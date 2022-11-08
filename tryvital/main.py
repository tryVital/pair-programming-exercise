from fastapi import FastAPI

from tryvital.api.api_v1.router import api_router


app = FastAPI(title="TryVital exercise")

app.include_router(api_router, prefix="/api/v1")


def run_server():
    import uvicorn
    uvicorn.run(f"{__name__}:app", port=5000, log_level="info", reload=True)

