from fastapi import FastAPI

# python -m uvicorn main:app --reload

app = FastAPI(title="training")

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}