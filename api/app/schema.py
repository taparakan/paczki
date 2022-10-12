from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ApiUser(BaseModel):
    user_id: int
    api_user_id: str
    email: str
    provider: str


#expiration date in unix epoch time
class UserToken(BaseModel):
    id: int
    token: str
    user_id: int
    expires: int