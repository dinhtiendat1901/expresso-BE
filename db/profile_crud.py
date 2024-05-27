from sqlalchemy.orm import Session
from sqlalchemy import update
from .models.profile import Profile
from schemas.profile import ProfileCreate, ProfileUpdate
from sqlalchemy import or_


def get_total_profiles(db: Session):
    return db.query(Profile).count()


def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()


def get_profiles(db: Session, skip: int = 0, limit: int = 100, search: str | None = None):
    query = db.query(Profile)
    if search:
        query = query.filter(or_(Profile.name.ilike(f'%{search}%'), Profile.description.ilike(f'%{search}%')))
    return query.offset(skip).limit(limit).all()


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


def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()
        return db_profile
