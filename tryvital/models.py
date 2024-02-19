import uuid
from datetime import date

from pydantic import BaseModel

class Activity(BaseModel):
    id: uuid.UUID
    user_id: str
    date: date
    steps: int
    calories: int


class Credentials(BaseModel):
    access_token: str
