from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UsersListSchemas(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    hashed_password: Optional[str] = None
    role: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
