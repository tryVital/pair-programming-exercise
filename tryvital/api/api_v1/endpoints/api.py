from datetime import date

from fastapi import APIRouter

from tryvital.models import Activity, Credentials

router = APIRouter()


@router.get("/activity")
async def get_activity(
    start_date: date,
    end_date: date,
    vital_user_id: str,
) -> list[Activity]:
    """
    Get stored activity data of a user.
    """
    return "Success"


@router.post("/fitbit/connect/{vital_user_id}")
async def connect_fitbit(vital_user_id: str) -> str:
    """
    Callback when a user has successfully authenticated with Fitbit.
    """

    credentials = Credentials(access_token="INTERVIEWER_TO_PROVIDE")

    print(f"Vital User ID: {vital_user_id}")

    return "Success"
