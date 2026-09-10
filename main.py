from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from starlette.responses import JSONResponse

from api.v1.router import api_v1_router
from database import get_session

# python -m uvicorn main:app --reload

app = FastAPI(title="training")
app.include_router(api_v1_router)
SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.get("/health", tags=["health"], status_code=200)
async def health(session: SessionDep):
    try:
        await session.execute(text("SELEsCT 1"))
        return {
            "status": "ok",
            "db": "ok",
        }
    except Exception:
        return JSONResponse({
            "status": "ok",
            "db": "error",
        }, status_code=503)
