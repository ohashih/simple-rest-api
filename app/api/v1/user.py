from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user

router = APIRouter()


@router.post("/users", response_model=UserRead)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
