from pydantic import BaseModel


class SessionData(BaseModel):
    username: str
    aai_state: str
