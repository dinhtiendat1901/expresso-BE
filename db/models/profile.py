from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from db.session import Base  # Import the Base class you created earlier

class Profile(Base):
    __tablename__ = 'profiles'  # Name of the table in your database

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True)
    description = Column(String(100), nullable=True)
    created_date = Column(TIMESTAMP, server_default=func.now())  # Use func.now() to get the current time and date

