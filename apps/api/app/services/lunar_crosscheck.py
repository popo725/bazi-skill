from __future__ import annotations

from datetime import date

from lunar_python import Solar


class LunarPythonCrossCheck:
    """Independent MIT-licensed cross-check against 6tail/lunar-python.

    This does not replace the project's own calculation rules. It records
    differences so QA can identify boundary-policy or algorithm discrepancies.
    """

    engine_name = "6tail/lunar-python"

    def calculate_pillars(
        self,
        solar_date: date,
        hour: int,
        minute: int,
    ) -> dict[str, str]:
        solar = Solar.fromYmdHms(
            solar_date.year,
            solar_date.month,
            solar_date.day,
            hour,
            minute,
            0,
        )
        eight_char = solar.getLunar().getEightChar()
        return {
            "year": eight_char.getYear(),
            "month": eight_char.getMonth(),
            "day": eight_char.getDay(),
            "hour": eight_char.getTime(),
        }

    @staticmethod
    def compare(primary_pillars: dict, secondary: dict[str, str]) -> dict:
        primary = {
            "year": primary_pillars["year"][0] + primary_pillars["year"][1],
            "month": primary_pillars["month"][0] + primary_pillars["month"][1],
            "day": primary_pillars["day"][0] + primary_pillars["day"][1],
            "hour": primary_pillars["hour"][0] + primary_pillars["hour"][1],
        }
        mismatches = {
            key: {"primary": primary[key], "secondary": secondary[key]}
            for key in primary
            if primary[key] != secondary[key]
        }
        return {
            "matched": not mismatches,
            "primary": primary,
            "secondary": secondary,
            "mismatches": mismatches,
            "note": (
                "A mismatch is a QA signal, not automatic proof that either engine is wrong; "
                "day-boundary, true-solar-time and school-specific rules may differ."
            ),
        }
