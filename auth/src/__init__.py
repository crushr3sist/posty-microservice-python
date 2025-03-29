from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


class PostyAuth(FastAPI):
    def __init__(self, *, title="posty auth"):
        super().__init__(title=title)
        self.register_endpoints()

    def register_middleware(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.add_middleware(GZipMiddleware)

    def register_endpoints(self):
        from src.users.endpoints import user_router

        self.include_router(user_router)

    def register_config(self): ...


posty_auth = PostyAuth()
from .inst_modifier import *
