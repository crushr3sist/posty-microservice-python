from asyncio.log import logger

import psycopg2
import sqlalchemy
import sqlalchemy.exc

import src
from src.database import init_db


@src.posty_auth.on_event("startup")
async def init_database():
    try:
        await init_db()
    except (
        sqlalchemy.exc.OperationalError,
        psycopg2.OperationalError,
    ) as p:
        logger.error(f"database connection error: {p}")
        for _ in range(0, 5):
            try:
                await init_db()
            except (sqlalchemy.exc.OperationalError, psycopg2.OperationalError) as p:
                print("db connection hitch, retrying")
            else:
                break
        raise Exception("your db failed to connect")
