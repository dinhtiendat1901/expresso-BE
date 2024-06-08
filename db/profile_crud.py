from datetime import date

from sqlalchemy.orm import Session
from .models.profile import Profile
from schemas.profile import ProfileCreate, ProfileUpdate
from sqlalchemy import or_, desc


def get_total_profiles(db: Session, search: str | None = None,
                       start_date: date | None = None, end_date: date | None = None):
    query = db.query(Profile)
    if search:
        query = query.filter(or_(Profile.name.ilike(f'%{search}%'), Profile.description.ilike(f'%{search}%')))
    if start_date and end_date:
        query = query.filter(Profile.created_date >= start_date, Profile.created_date <= end_date)
    elif start_date:
        query = query.filter(Profile.created_date >= start_date)
    elif end_date:
        query = query.filter(Profile.created_date <= end_date)
    return query.count()


def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()


def get_profiles(db: Session, skip: int = 0, limit: int = 100, search: str | None = None,
                 start_date: date | None = None, end_date: date | None = None):
    query = db.query(Profile)
    if search:
        query = query.filter(or_(Profile.name.ilike(f'%{search}%'), Profile.description.ilike(f'%{search}%')))
    if start_date and end_date:
        query = query.filter(Profile.created_date >= start_date, Profile.created_date <= end_date)
    elif start_date:
        query = query.filter(Profile.created_date >= start_date)
    elif end_date:
        query = query.filter(Profile.created_date <= end_date)

    query = query.order_by(desc(Profile.created_date))
    profiles = query.offset(skip).limit(limit).all()
    return profiles


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(name=profile.name, description=profile.description)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def update_profile(db: Session, profile_id: int, update_data: ProfileUpdate):
    db.query(Profile).filter(Profile.id == profile_id).update({
        Profile.name: update_data.name,
        Profile.description: update_data.description
    }, synchronize_session='fetch')
    db.commit()
    return db.query(Profile).filter(Profile.id == profile_id).first()


def delete_profiles(db: Session, profile_ids: list[int]):
    # Query to find all profiles with IDs in the provided list and delete them
    db.query(Profile).filter(Profile.id.in_(profile_ids)).delete(synchronize_session='fetch')
    db.commit()
