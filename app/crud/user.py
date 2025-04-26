from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.user import User as UserModel
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate) -> UserModel:
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session) -> List[UserModel]:
    return db.query(UserModel).all()


def get_user_by_id(db: Session, user_id: int) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def update_user(db: Session, db_user: UserModel, updates: UserCreate) -> UserModel:
    if updates.name is not None:
        db_user.name = updates.name
    if updates.email is not None:
        db_user.email = updates.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: UserModel) -> None:
    db.delete(db_user)
    db.commit()
