from pydantic import BaseModel
from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")


class Meta(BaseModel):
    status: int
    message: str


class APIResponse(GenericModel, Generic[T]):
    data: Optional[T]
    meta: Meta
