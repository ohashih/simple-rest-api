from fastapi import FastAPI, Request, status, Depends, Response, HTTPException
from sqlalchemy.orm import Session

from typing import List

from app.core.database import get_db, engine
from app.crud import user as user_crud
from app.models.user import Base
from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.response import APIResponse

app = FastAPI()
users: List[User] = []

Base.metadata.create_all(bind=engine)


@app.get(
    "/api/users",
    response_model=APIResponse[List[User]],
    status_code=status.HTTP_200_OK,
)
def get_users(db: Session = Depends(get_db)):
    return {
        "data": user_crud.get_users(db),
        "meta": {
            "status": status.HTTP_200_OK,
            "message": "Users retrieved successfully",
        },
    }


@app.post(
    "/api/users",
    response_model=APIResponse[User],
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
):
    db_user = user_crud.create_user(db, user)
    location_url = str(request.url_for("get_user_by_id", user_id=db_user.id))
    response.headers["Location"] = location_url

    return {
        "data": db_user,
        "meta": {
            "status": status.HTTP_201_CREATED,
            "message": "User created successfully",
        },
    }


@app.get(
    "/api/users/{user_id}",
    response_model=APIResponse[User],
    status_code=status.HTTP_200_OK,
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)
    if user is None:
        return {
            "data": None,
            "meta": {"status": status.HTTP_404_NOT_FOUND, "message": "User not found"},
        }
    return {
        "data": user,
        "meta": {
            "status": status.HTTP_200_OK,
            "message": "user retrieved successfully",
        },
    }


@app.put(
    "/api/users/{user_id}",
    response_model=APIResponse[User],
    status_code=status.HTTP_200_OK,
)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)) -> User:
    db_user = user_crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    user_crud.update_user(db, db_user, user)
    return {
        "data": db_user,
        "meta": {
            "status": status.HTTP_200_OK,
            "message": "User update successfully",
        },
    }


@app.delete(
    "/api/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    db_user = user_crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user_crud.delete_user(db, db_user)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
