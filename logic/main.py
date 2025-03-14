from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def logic_endpoint():
    return {"message":"reached logic domain"}

