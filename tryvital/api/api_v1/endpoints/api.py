import uuid
from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from fitbit import fitbit_connected_callback, Credentials

router = APIRouter()


class Activity(BaseModel):
    id: uuid.UUID
    steps: int
    calories: int


@router.get("/activity")
async def get_activity(
    start_date: datetime,
    end_date: datetime,
    user_id: str,
) -> Activity:
    """Get activity data for a user."""
    return "Success"


@router.post("/fitbit/connect")
async def connect_fitbit(user_id: str) -> str:
    """This endpoint is called when a user connects their Fitbit account."""
    credentials = Credentials(access_token="foo", refresh_token="bar")
    fitbit_connected_callback(user_id, credentials)
    return "Success"
