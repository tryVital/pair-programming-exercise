from datetime import date, datetime

from .oura_sleep import SleepDocument

test1 = [
    SleepDocument(
        id="1234",
        contributors={},
        day=date(2023, 1, 10),
        score=75.6,
        timestamp=datetime(2023, 1, 9, 22, 0, 0),
        duration=3600 * 8,
    ),
    SleepDocument(
        id="1234",
        contributors={},
        day=date(2023, 1, 9),
        score=75.6,
        timestamp=datetime(2023, 1, 9, 20, 0, 0),
        duration=3678,
    ),
]