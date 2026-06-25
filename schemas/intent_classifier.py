from pydantic import BaseModel, Field
from typing import Literal

class IntentClassifier(BaseModel):
    message_intent: Literal["chat", "knowledge", "code"] = Field(..., description="Classify whether the user just wants to chat, ask for knowledge, or change code in the project")
