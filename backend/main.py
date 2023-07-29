# backend/main.py
from fastapi import FastAPI
from backend.api.grammar import router as grammar_router
from backend.database import engine, metadata, database

app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup_db():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()

app.include_router(grammar_router, prefix="/grammar", tags=["grammar"])