from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from data.database import SessionLocal, engine
from model import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def top():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
