from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.post("/activity")
async def get_activity(
    start_date: datetime,
    end_date: datetime,
    provider: str,
    user_id: str,
):
    return "Success"
