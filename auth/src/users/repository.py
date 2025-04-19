from typing import AsyncGenerator, Optional

import arrow
from jose import jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import Config
from src.database import SessionLocal
from src.users.models import UserModel, UserSchema


def generate_token(user: UserSchema) -> str:

    return jwt.encode(
        {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "exp": arrow.utcnow().shift(months=1).timestamp(),
        },
        Config.jwt_secret,
        "HS256",
    )


def decode_token(token: str):
    return jwt.decode(token, Config.jwt_secret, "HS256")


def validate_token_expire(token: str) -> bool:
    return dict(decode_token(token))["exp"] > arrow.utcnow().timestamp()


def hash_password(password):
    return Config.password_context.hash(password)


async def get_user(db: AsyncSession, email):
    try:
        async with db.begin():
            result = await db.execute(
                select(UserModel).filter(UserModel.email == email)
            )
            return result.scalars().first()
    except Exception as e:
        await db.rollback()
        return e


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


async def check_password(db, email, password) -> bool:
    user = await get_user(db, email)
    if isinstance(user, Exception) or user is None:
        return False
    return Config.password_context.verify(password, str(user.hashed_password))


async def create_user(db: AsyncSession, user: UserSchema):
    try:
        async with db.begin():
            user_to_commit = UserModel(
                email=user.email,
                username=user.username,
                hashed_password=user.hashed_password,
            )
            db.add(user_to_commit)
            await db.commit()
            
    except Exception as e:
        await db.rollback()
        return e
    return True


def update_user() -> Optional[bool]: ...


def delete_user() -> Optional[bool]: ...
