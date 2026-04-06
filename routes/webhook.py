from sqlmodel import SQLModel, Field, Session, select, Relationship
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import models
from db import get_session


router = APIRouter()


@router.post("/webhook", response_model=models.entries, status_code=201)
async def create_entry(
    webhook: models.entries, session: Session = Depends(get_session)
):
    """
    Create a new webhook entry in the database.
    """
    try:
        new_webhook = models.entries.model_validate(webhook)
        session.add(new_webhook)
        session.commit()
        session.refresh(new_webhook)
        return new_webhook

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating webhook: {str(e)}")
