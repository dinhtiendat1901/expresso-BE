from typing import List

from pydantic import BaseModel
from datetime import datetime


class ProfileBase(BaseModel):
    name: str
    description: str | None = None


class ProfileCreate(ProfileBase):
    pass  # No additional fields needed for creation


class ProfileUpdate(ProfileBase):
    pass  # No additional fields needed for update


class ProfileInDBBase(ProfileBase):
    id: int
    created_date: datetime

    class Config:
        from_attributes = True


class Profile(ProfileInDBBase):
    pass  # This schema will be used for reading data from the database


class ProfileInDB(ProfileInDBBase):
    pass  # This schema could be used for more detailed database interaction


class ProfileList(BaseModel):
    profiles: List[Profile]
    total: int
