import os
from fastapi import FastAPI
from routes import router as api_router
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
