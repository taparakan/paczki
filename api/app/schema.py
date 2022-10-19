from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str

class Parcel(BaseModel):
    id: int
    name: str
    from_locker_id: int
    to_locker_id: int
    sender_id: int
    receiver_id: int
    state: str

class ParcelLocker(BaseModel):
    id: int
    name: str