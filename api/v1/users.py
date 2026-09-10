from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import Pagination
from api.models.users import UsersModel
from api.schemas.base import PaginatedResponse
from api.schemas.users.schemas import UsersListSchemas
from database import get_session

router = APIRouter(tags=["users"])
SessionDep = Annotated[AsyncSession, Depends(get_session)]

@router.get("/users/", status_code=200, response_model=PaginatedResponse[UsersListSchemas])
async def users_list(
        session: SessionDep,
        pagination: Pagination,
):
    result = await session.execute(select(UsersModel).limit(pagination.limit).offset(pagination.offset))
    users = result.scalars().all()

    total = await session.execute(select(func.count()).select_from(UsersModel))
    total = total.scalar()
    return PaginatedResponse(
        items=users,
        total=total,
        limit=pagination.limit,
        offset=pagination.offset,

    )