from __future__ import annotations

from fastapi import FastAPI, HTTPException

from .schemas import BaziChartRequest, HealthResponse
from .services.bazi_service import BaziService


app = FastAPI(
    title="Traditional Culture Analysis API",
    version="0.1.0",
    description=(
        "Deterministic chart calculation API for a commercial traditional-culture "
        "analysis product. AI interpretation is intentionally separated from chart math."
    ),
)

_bazi = BaziService()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse()


@app.post("/v1/bazi/chart")
def calculate_bazi_chart(payload: BaziChartRequest) -> dict:
    try:
        return _bazi.calculate(payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
