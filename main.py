from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from starlette.responses import JSONResponse

from database import get_session

# python -m uvicorn main:app --reload

app = FastAPI(title="training")

SessionDep = Annotated[AsyncSession, Depends(get_session)]

@app.get("/health")
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