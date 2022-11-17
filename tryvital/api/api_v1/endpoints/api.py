import uuid
from datetime import date, datetime

from fastapi import APIRouter
from pydantic import BaseModel

from fitbit import fitbit_connected_callback, Credentials

router = APIRouter()


class Activity(BaseModel):
    id: uuid.UUID
    user_id: str
    date: date
    steps: int
    calories: int


@router.get("/activity")
async def get_activity(
    start_date: date,
    end_date: date,
    user_id: str,
) -> Activity:
    """Get activity data for a user."""
    return "Success"


@router.post("/fitbit/connect/{user_id}")
async def connect_fitbit(user_id: str) -> str:
    """This endpoint is called when a user connects their Fitbit account."""
    credentials = Credentials(access_token="foo", refresh_token="bar")
    fitbit_connected_callback(user_id, credentials)
    return "Success"
