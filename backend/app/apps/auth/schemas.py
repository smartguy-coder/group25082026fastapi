from pydantic import BaseModel


class RefreshTokenRequestSchema(BaseModel):
    refresh_token: str


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
