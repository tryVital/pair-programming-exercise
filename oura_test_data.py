from datetime import date, datetime

from .oura_sleep import SleepDocument

test1 = [
    SleepDocument(
        id="1234",
        contributors={
            "efficiency": 78.0,
        },
        day=date(2023, 1, 10),
        score=75.6,
        timestamp=datetime(2023, 1, 9, 22, 0, 0),
        duration=3600 * 6,
    ),
    SleepDocument(
        id="1234",
        contributors={
            "efficiency": 91.0,
        },
        day=date(2023, 1, 10),
        score=75.6,
        timestamp=datetime(2023, 1, 10, 4, 30, 0),
        duration=3600 * 3,
    ),
    SleepDocument(
        id="1234",
        contributors={
            "efficiency": 82.0,
        },
        day=date(2023, 1, 9),
        score=75.6,
        timestamp=datetime(2023, 1, 9, 20, 0, 0),
        duration=3678,
    ),
]