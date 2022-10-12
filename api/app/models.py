from sqlmodel import SQLModel, Field
from typing import Optional

class ApiUser(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    api_user_id: str
    email: str
    provider: str

class UserToken(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    token: str
    user_id: int
    expires: int
    