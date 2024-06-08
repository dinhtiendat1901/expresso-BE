from datetime import date

from sqlalchemy.orm import Session
from db.profile_crud import create_profile, get_profile, get_profiles, update_profile, delete_profiles, \
    get_total_profiles
from schemas.profile import ProfileCreate, ProfileUpdate


def get_total_profiles_service(db: Session):
    return get_total_profiles(db)


def create_profile_service(db: Session, profile_data: ProfileCreate):
    # Business logic can be added here, e.g., validation, manipulation of the data before saving
    return create_profile(db, profile_data)


def get_profile_service(db: Session, profile_id: int):
    # Additional business logic can be processed here before returning the data
    return get_profile(db, profile_id)


def list_profiles_service(db: Session, skip: int = 0, limit: int = 100, search: str | None = None,
                          start_date: date | None = None, end_date: date | None = None):
    return get_profiles(db, skip=skip, limit=limit, search=search, start_date=start_date, end_date=end_date)


def update_profile_service(db: Session, profile_id: int, profile_data: ProfileUpdate):
    # Check or modify data before updating
    return update_profile(db, profile_id, profile_data)


def delete_profiles_service(db: Session, profile_ids: list[int]):
    delete_profiles(db, profile_ids)
