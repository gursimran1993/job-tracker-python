from fastapi import FastAPI, Depends
from app.core.config import settings
from datetime import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db
app = FastAPI(title=settings.app_name)

@app.get("/")
async def home():
    return {"message":"Welcome to the job tracker API"}

@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    db.execute(text("SELECT 1"))
    return{"status":"ok", "database": "ok"}

async def get_time():
    return datetime.now().strftime("%H:%M:%S")

@app.get("/time")
async def show_time(now:Annotated[str,Depends(get_time)]):
     return{"time": now}
    #datetime.now().strftime("%H:%M:%S")
