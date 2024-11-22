from contextlib import asynccontextmanager
from fastapi import FastAPI

from tryvital.api.api_v1.router import api_router
from tryvital.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    # Shutdown: clean up code
    pass


app = FastAPI(title="Pair Programming Exercise", lifespan=lifespan)

app.include_router(api_router, prefix="/v1")

def run_server():
    import uvicorn
    uvicorn.run(f"{__name__}:app", port=8000, log_level="info", reload=True)

