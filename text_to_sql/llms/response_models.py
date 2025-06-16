from pydantic import BaseModel


class DemoResponse(BaseModel):
    name: str | None
    age: int | None
