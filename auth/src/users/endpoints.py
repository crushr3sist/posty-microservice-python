from fastapi import APIRouter, Body, Depends
from sqlalchemy import select
from src.users.models import UserModel
from src.users.repository import create_user, get_db

user_router = APIRouter()


@user_router.get("/")
async def auth_index():
    return {"message", "you've reached the auth domain"}


@user_router.post("/login")
async def auth_login(login_form=Body(), db=Depends(get_db)):
    print(login_form)
    return {"message", "you've reached the auth login endpoint"}


@user_router.post("/register")
async def auth_register(reg_form=Body(), db=Depends(get_db)):
    try:
        result = await create_user(db, reg_form)
        print(result)
        return {"message": "user successfully created", "status": result}
    except Exception as e:
        return {"message": "/register error", "error:": e}


@user_router.get("/get_users")
async def get_users_all(db=Depends(get_db)):
    users = await db.execute(select(UserModel))
    return users.scalars().all()
