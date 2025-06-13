from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class ChatMessage(BaseModel):
    role: MessageRole
    content: str
    timestamp: datetime = datetime.now()
    session_id: str
    message_id: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    session_id: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: datetime = datetime.now()
    crisis_detected: bool = False
    sentiment_score: Optional[float] = None

class CrisisAlert(BaseModel):
    session_id: str
    user_id: Optional[str]
    message: str
    crisis_score: float
    timestamp: datetime = datetime.now()
    keywords_detected: List[str] = []