# Pair programming exercise

## Installation guide

Before installation, you must have python (>3.6) and poetry already installed in your system.

```bash
poetry shell
poetry install
```

### Running the API

```bash
poetry run uvicorn tryvital.main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [69443] using WatchFiles
INFO:     Started server process [69448]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Project structure

```
├── __init__.py
├── api
│   ├── __init__.py
│   └── api_v1
│       ├── __init__.py
│       ├── endpoints
│       │   ├── __init__.py
│       │   └── api.py  # Fill activity endpoint here.
│       └── router.py
|── fitbit.py # Fitbit related code.
└── main.py
```

### Task

Build an endpoint ([here](tryvital/api/api_v1/endpoints/api.py)) that fetches Fitbit activity data and saves it in the db.

API documentation for Fitbit activity:

<https://dev.fitbit.com/build/reference/web-api/activity/get-daily-activity-summary/>
