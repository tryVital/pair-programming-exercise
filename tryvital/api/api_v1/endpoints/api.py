from datetime import date
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncEngine
from tryvital.db import get_engine, read_query, write_query
from tryvital.models import Credentials

router = APIRouter()


@router.get("/activity")
async def get_activity(
    start_date: date,
    end_date: date,
    vital_user_id: str,
) -> Any:
    """
    Get stored activity data of a user.
    """
    await read_query("SELECT ...")
    return "Success"


@router.post("/fitbit/connect/{vital_user_id}")
async def connect_fitbit(vital_user_id: str) -> str:
    """
    Callback when a user has successfully authenticated with Fitbit.
    """

    credentials = Credentials(access_token="INTERVIEWER_TO_PROVIDE")

    print(f"Vital User ID: {vital_user_id}")

    await write_query("INSERT INTO ...")
    return "Success"
