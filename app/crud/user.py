from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(UserModel).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()
