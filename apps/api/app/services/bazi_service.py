from __future__ import annotations

from datetime import date

from scripts import pai_pan

from ..schemas import BaziChartRequest
from .lunar_crosscheck import LunarPythonCrossCheck


class BaziService:
    """Adapter around the current deterministic chart engine.

    HTTP handlers should not depend directly on scripts.pai_pan. This adapter
    is the seam for independent calendar cross-checks, true-solar-time support,
    engine-version metadata and future structured rule IDs.
    """

    engine_name = "bazi-skill-pai-pan"
    engine_version = "legacy-v1"

    def __init__(self) -> None:
        self.crosscheck = LunarPythonCrossCheck()

    @staticmethod
    def _parse_clock(value: str | None) -> tuple[int | None, int | None]:
        if not value:
            return None, None
        try:
            hour_text, minute_text = value.split(":", 1)
            hour, minute = int(hour_text), int(minute_text)
        except (TypeError, ValueError) as exc:
            raise ValueError("birth_time must use HH:MM") from exc
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError("birth_time must use a valid 24-hour HH:MM value")
        return hour, minute

    def calculate(self, payload: BaziChartRequest) -> dict:
        try:
            solar_date = date.fromisoformat(payload.solar_date)
        except ValueError as exc:
            raise ValueError("solar_date must use YYYY-MM-DD") from exc

        hour, minute = self._parse_clock(payload.birth_time)

        result = pai_pan.compute(
            solar_date=solar_date,
            hour=hour,
            minute=minute,
            shichen=payload.shichen,
            sex=payload.sex,
            place=payload.birth_place,
        )

        verification = {
            "status": "not_run",
            "reason": "Exact clock time is required for independent cross-check.",
        }
        if hour is not None and minute is not None:
            secondary = self.crosscheck.calculate_pillars(solar_date, hour, minute)
            verification = {
                "status": "completed",
                "engine": self.crosscheck.engine_name,
                **self.crosscheck.compare(result["pillars"], secondary),
            }

        # Keep deterministic facts separate from any future AI interpretation.
        return {
            "engine": {
                "name": self.engine_name,
                "version": self.engine_version,
            },
            "input": {
                "solar_date": payload.solar_date,
                "birth_time": payload.birth_time,
                "shichen": payload.shichen,
                "sex": payload.sex,
                "birth_place": payload.birth_place,
            },
            "chart": {
                "solar_text": result["solar_text"],
                "lunar_text": result["lunar_text"],
                "shichen_text": result["shichen_text"],
                "zishi": result["zishi"],
                "pillars": result["pillars"],
                "forward": result["forward"],
                "qiyun_text": result["qiyun_text"],
                "dayun_rows": result["dayun_rows"],
                "current_year": result["current_year"],
                "current_gz": result["current_gz"],
                "shensha": result["shensha_lines"],
                "warnings": result["warnings"],
            },
            "verification": verification,
            "disclaimer": "Traditional-culture and entertainment reference only; not a basis for medical, legal, financial, or other high-stakes decisions.",
        }
