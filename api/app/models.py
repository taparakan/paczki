from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
    username: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
class Parcel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    from_locker_id: int
    to_locker_id: int
    sender_id: int
    receiver_id: int
    state: str

class ParcelLocker(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
