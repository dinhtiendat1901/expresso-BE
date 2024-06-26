from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy.orm import Session
from schemas.profile import ProfileCreate, Profile, ProfileUpdate
from services.profile_service import (
    create_profile_service,
    get_profile_service,
    list_profiles_service,
    update_profile_service,
    delete_profiles_service,
    get_total_profiles_service
)
from api.dependencies.database import get_db

router = APIRouter()


@router.get("/profiles/total", response_model=int)
def read_total_profiles(search: str = None, start_date: date = Query(None),
                        end_date: date = Query(None), db: Session = Depends(get_db)):
    total = get_total_profiles_service(db, search=search, start_date=start_date, end_date=end_date)
    return total


@router.post("/profiles/", response_model=Profile)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return create_profile_service(db, profile)


@router.get("/profiles/{profile_id}", response_model=Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = get_profile_service(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/profiles/", response_model=list[Profile])  # Adjust the response model if necessary
def read_profiles(skip: int = 0, limit: int = 100, search: str = None, start_date: date = Query(None),
                  end_date: date = Query(None), db: Session = Depends(get_db)):
    return list_profiles_service(db, skip=skip, limit=limit, search=search, start_date=start_date, end_date=end_date)


@router.put("/profiles/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, profile: ProfileUpdate, db: Session = Depends(get_db)):
    updated_profile = update_profile_service(db, profile_id, profile)
    if updated_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated_profile


@router.delete("/profiles/")
def delete_profiles(profile_ids: list[int] = Body(...), db: Session = Depends(get_db)):
    delete_profiles_service(db, profile_ids)
    return {"message": "Profiles deleted successfully", "profile_ids": profile_ids}
