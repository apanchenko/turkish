# backend/models/__init__.py
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

GrammarRule = Table(
    "grammar_rule",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("content", String),
)

Phrase = Table(
    "phrase",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("content", String),
    Column("translation", String),
)
