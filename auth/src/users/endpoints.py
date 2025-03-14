from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/")
async def auth_index():
    return {"message", "you've reached the auth domain"}

@user_router.get("/login")
async def auth_login():
    return {"message", "you've reached the auth login endpoint"}


@user_router.get("/register")
async def auth_register():
    return {"message", "you've reached the auth register endpoint"}