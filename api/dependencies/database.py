from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import SessionLocal
from db.models.profile import Profile

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
