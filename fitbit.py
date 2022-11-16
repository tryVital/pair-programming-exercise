from pydantic import BaseModel


class Credentials(BaseModel):
    access_token: str
    refresh_token: str


def fitbit_connected_callback(user_id: str, credentials: Credentials):
    """Callback for when a user connects their Fitbit account."""
    ...
