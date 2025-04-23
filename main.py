from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from typing import List
from app.schemas.user import User, UserCreate
from app.schemas.response import APIResponse
from app.models.user import Base
from app.core.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

users: List[User] = []
id_counter = 1


@app.get(
    "/api/users",
    response_model=APIResponse[List[User]],
    status_code=status.HTTP_200_OK,
)
def get_users():
    return {
        "data": users,
        "meta": {"status": 200, "message": "Users retrieved successfully"},
    }


@app.post(
    "/api/users",
    response_model=APIResponse[User],
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserCreate, request: Request):
    global id_counter
    new_user = User(id=id_counter, name=user.name, email=user.email)
    users.append(new_user)
    location_url = str(request.url_for("get_user_by_id", user_id=new_user.id))
    id_counter += 1
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        headers={"Location": location_url},
        content={
            "data": new_user.dict(),
            "meta": {
                "status": status.HTTP_201_CREATED,
                "message": "User created successfully",
            },
        },
    )


@app.get(
    "/api/users/{user_id}",
    response_model=APIResponse[User],
    status_code=status.HTTP_200_OK,
    name="get_user_by_id",
)
def get_user_by_id(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "data": None,
                "meta": {"status": 404, "message": "User not found."},
            },
        )
    return {
        "data": user.dict(),
        "meta": {
            "status": status.HTTP_200_OK,
            "message": "user retrived successfully",
        },
    }
