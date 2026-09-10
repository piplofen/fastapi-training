from typing import Annotated
from fastapi import Query, Depends

class PaginationParams:
    def __init__(
        self,
        limit: Annotated[int, Query(ge=1, le=100)] = 20,
        offset: Annotated[int, Query(ge=0)] = 0,
    ):
        self.limit = limit
        self.offset = offset

Pagination = Annotated[PaginationParams, Depends()]