from pydantic import BaseModel


class Memory(BaseModel):
    remember: bool
    key: str
    value: str


class ChatResponse(BaseModel):
    reply: str
    memory: Memory