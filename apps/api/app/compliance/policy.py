from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class RiskLevel(StrEnum):
    LOW = "low"
    REVIEW = "review"
    BLOCK = "block"


@dataclass(frozen=True)
class PolicyDecision:
    level: RiskLevel
    reason: str


BLOCKED_PATTERNS = (
    "一定会死",
    "必死",
    "一定得癌",
    "保证发财",
    "包发财",
    "交钱消灾",
    "花钱改命",
    "保证复合",
    "保证离婚",
)

REVIEW_PATTERNS = (
    "什么时候死",
    "会得什么病",
    "能不能把全部钱买",
    "借钱投资",
    "替我决定离婚",
    "替我决定结婚",
)


def classify_user_request(text: str) -> PolicyDecision:
    """Very small deterministic first-pass gate.

    This is intentionally not presented as a complete moderation system. A
    production build should combine deterministic policy, model moderation,
    audit logging, locale-specific legal review, and regression tests.
    """

    normalized = (text or "").strip()
    if any(pattern in normalized for pattern in BLOCKED_PATTERNS):
        return PolicyDecision(
            RiskLevel.BLOCK,
            "Request asks for coercive/guaranteed or high-risk fortune claims.",
        )
    if any(pattern in normalized for pattern in REVIEW_PATTERNS):
        return PolicyDecision(
            RiskLevel.REVIEW,
            "Request touches medical, financial, relationship or mortality decisions.",
        )
    return PolicyDecision(RiskLevel.LOW, "No initial high-risk pattern detected.")
