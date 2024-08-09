from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password_hash: str
    created_at: str
    updated_at: str