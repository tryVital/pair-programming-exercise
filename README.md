# Pair programming exercise

## Installation guide

Before installation, you must have Python 3.10-3.12 and Poetry already installed in your system.

```bash
poetry shell
poetry install
```

### Running the API

```bash
poetry run server
```

Expected standout output:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [69443] using WatchFiles
INFO:     Started server process [69448]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

#### Useful resources

Things FastAPI gives you out-of-the-box:

* Swagger UI (http://127.0.0.1:8000/docs) with API Playground.
* Redoc (http://127.0.0.1:8000/redoc) for a prettier look at the OpenAPI schema.

## Project structure

```
tryvital
├── api
│   └── api_v1
│       ├── endpoints
│       │   └── api.py  # Endpoints are defined here.
│       └── router.py
|── models.py           # Pre-defined Pydantic models
└── main.py
```

### Exercise Goal

There are two deliverables:

1. Implement the callback endpoint: `POST /v1/fitbit/connect/{vital_user_id}`
  * It should fetch 7 days worth of (historical) activity daily summary data from Fitbit API.
  * It should then store it in a method of your own choice.

2. Implement the query endpoint: `GET /v1/activity`
  * It should query the activity daily summary data being stored in Deliverable 1.
  * The result must be filtered in accordance to the input date range.
  * The date range should be start inclusive and end inclusive.

Notes:

* This exercise does not involve going through the actual Fitbit OAuth flow.
* Fitbit API documentation: Get Daily Activity Summary
  * https://dev.fitbit.com/build/reference/web-api/activity/get-daily-activity-summary/
* A valid Fitbit API access token would be provided by the interviewer at the start of the session.

![Flow Diagram](/flow-diagram.png)
