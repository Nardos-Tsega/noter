from pydantic import BaseModel

class Note(BaseModel):
    title: str
    content: str
    is_completed: bool 
    created_at: str
    updated_at: str