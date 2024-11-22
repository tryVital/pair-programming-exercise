from datetime import date
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncEngine
from tryvital.db import get_engine
from tryvital.models import Credentials

router = APIRouter()


@router.get("/activity")
async def get_activity(
    start_date: date,
    end_date: date,
    vital_user_id: str,
    db: AsyncEngine = Depends(get_engine)
) -> Any:
    """
    Get stored activity data of a user.
    """
    return "Success"


@router.post("/fitbit/connect/{vital_user_id}")
async def connect_fitbit(vital_user_id: str, db: AsyncEngine = Depends(get_engine)) -> str:
    """
    Callback when a user has successfully authenticated with Fitbit.
    """

    credentials = Credentials(access_token="INTERVIEWER_TO_PROVIDE")

    print(f"Vital User ID: {vital_user_id}")

    return "Success"
