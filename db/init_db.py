from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from db.session import Base, engine
from db.models.profile import Profile  # Import all your models here


def init_db():
    # This will create all tables according to the models defined
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
