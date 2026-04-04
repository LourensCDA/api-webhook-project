from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Session,
    select,
    Relationship,
    Column,
    JSON,
)
from typing import Dict


class users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    apy_key: str = Field(default=None, max_length=255)


class leads(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=255)
    phone: str = Field(max_length=20)
    user_id: int = Field(default=None, foreign_key="users.id")
    campaign_id: int = Field(default=None)


class calls(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    lead_id: int = Field(default=None, foreign_key="leads.id")
    create_date: str = Field(max_length=50)
    duration: int = Field(default=0)
    outcome: str = Field(max_length=50)


class hooks(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    active: bool = Field(default=True)


class entries(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    hook_id: int = Field(default=None, foreign_key="hooks.id")
    data: Dict = Field(default_factory=dict, sa_column=Column(JSON))
