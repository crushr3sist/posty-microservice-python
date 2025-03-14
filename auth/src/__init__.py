from fastapi import FastAPI


class PostyAuth(FastAPI):
    def __init__(self, *, title="posty auth"):
        super().__init__(title=title)
        self.register_endpoints()
    
    def register_middleware(self):
        ...
    def register_endpoints(self):
        from src.users.endpoints import user_router
        self.include_router(user_router)
    def register_config(self):
        ...

posty_auth=PostyAuth()
