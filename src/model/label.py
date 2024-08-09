from pydantic import BaseModel

class Label(BaseModel):
    name: str
    created_at: str
    updated_at: str