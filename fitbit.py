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
    refresh_token: str


def fitbit_connected_callback(user_id: str, credentials: Credentials):
    """Callback for when a user connects their Fitbit account."""
    ...
