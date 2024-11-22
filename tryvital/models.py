from pydantic import BaseModel

class Credentials(BaseModel):
    access_token: str
