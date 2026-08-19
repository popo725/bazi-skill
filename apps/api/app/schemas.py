from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator


SexForTraditionalRules = Literal["男", "女"]


class BaziChartRequest(BaseModel):
    """Input accepted by the deterministic Bazi chart endpoint.

    V1 deliberately keeps the payload narrow. Name is not required because it
    is not needed for chart calculation and would create unnecessary personal
    data collection.
    """

    solar_date: str = Field(..., description="Gregorian date, YYYY-MM-DD")
    birth_time: str | None = Field(
        default=None,
        description="Clock time HH:MM. Mutually exclusive with shichen.",
    )
    shichen: Literal[
        "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"
    ] | None = None
    sex: SexForTraditionalRules
    birth_place: str | None = Field(
        default=None,
        description="Free-text place for display/boundary warning in legacy engine.",
        max_length=120,
    )

    @model_validator(mode="after")
    def validate_time_choice(self):
        if self.birth_time and self.shichen:
            raise ValueError("birth_time and shichen are mutually exclusive")
        return self


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    service: str = "fortune-commercial-api"
    version: str = "0.1.0"
