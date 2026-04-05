from sqlmodel import SQLModel, Field, Session, select, Relationship
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import models
from db import get_session


router = APIRouter()


@router.get("/leads", response_model=List[models.leads])
async def leads(session: Session = Depends(get_session)):
    statement = select(models.leads)
    return session.exec(statement).all()
