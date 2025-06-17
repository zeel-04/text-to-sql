from typing import Literal, TypedDict, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class Message(TypedDict):
    """Standard LLM message format following OpenAI/industry conventions."""

    role: Literal["system", "user", "assistant"]
    content: str
