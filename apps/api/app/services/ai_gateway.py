from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class ReadingContext:
    chart: dict[str, Any]
    rule_evidence: list[dict[str, Any]]
    locale: str = "zh-CN"
    product_tier: str = "free"


@dataclass(frozen=True)
class GeneratedReading:
    text: str
    provider: str
    model: str
    prompt_version: str
    generated_content_label: bool = True


class AIReadingProvider(Protocol):
    """Provider-neutral contract for the interpretation layer.

    Deterministic chart calculation must happen before this interface is called.
    Implementations must not change pillars or other engine facts.
    """

    def generate_bazi_reading(self, context: ReadingContext) -> GeneratedReading:
        ...


class AIProviderNotConfigured(RuntimeError):
    pass
