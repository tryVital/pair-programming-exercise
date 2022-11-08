from fastapi import APIRouter

from tryvital.api.api_v1.endpoints import historical

api_router = APIRouter()
api_router.include_router(historical.router, tags=["historical"], prefix="/historical")
