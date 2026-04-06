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
    """
    Get all leads from the database.
    """
    statement = select(models.leads)
    return session.exec(statement).all()


@router.post("/leads", response_model=models.leads, status_code=201)
async def create_lead(lead: models.leads, session: Session = Depends(get_session)):
    """
    Create a new lead in the database.
    """
    try:
        new_lead = models.leads.model_validate(lead)
        session.add(new_lead)
        session.commit()
        session.refresh(new_lead)
        return new_lead

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating lead: {str(e)}")
