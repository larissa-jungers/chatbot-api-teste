from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4
from datetime import datetime

class Session(BaseModel):
    session_id: str
    technician_id: str
    chat_started: bool = False
    notes: Optional[str] = None
    messages: List[str] = []

    @classmethod
    def create(cls, technician_id: str, notes: Optional[str] = None):
        return cls(
            session_id=str(uuid4()),
            technician_id=technician_id,
            chat_started=True,
            notes=notes,
            messages=[]
        )