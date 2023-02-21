from datetime import date, datetime
from typing import Dict, Iterator, Literal, Optional

from pydantic import BaseModel, ConstrainedInt


class _Percent(ConstrainedInt):
    ge: int = 1
    le: int = 100


_ContributorKeys = Literal[
    "deep_sleep",
    "efficiency",
    "latency",
    "rem_sleep",
    "restfulness",
    "timing",
    "total_sleep",
]

_Contributors = Dict[_ContributorKeys, Optional[_Percent]]


class SleepDocument(BaseModel):
    id: str
    contributors: _Contributors
    day: date
    score: Optional[float]
    timestamp: datetime


def merge_sleep(raw_sleep: Iterator[SleepDocument]) -> Iterator[SleepDocument]:
    assert False, raw_sleep


__all__ = ["SleepDocument", "merge_sleep"]
