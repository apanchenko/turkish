# backend/api/grammar.py
from fastapi import APIRouter, HTTPException
from backend.models import GrammarRule, Phrase
from backend.database import database

router = APIRouter()

@router.get("/{item_id}")
async def read_item(item_id: int):
    query = GrammarRule.select().where(GrammarRule.c.id == item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/phrases")
async def get_phrases():
    query = Phrase.select()
    return await database.fetch_all(query)