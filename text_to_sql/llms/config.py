from typing import Any

from pydantic import BaseModel, Field


class BaseConfig(BaseModel):
    model: str | None = Field(None, description="Model name to use")
    temperature: float | None = Field(
        None, ge=0.0, le=2.0, description="Temperature for generation"
    )
    max_completion_tokens: int | None = Field(
        None, gt=0, description="Maximum completion tokens"
    )
    top_p: float | None = Field(
        None, ge=0.0, le=1.0, description="Top-p value for generation"
    )
    custom_kwargs: dict[str, Any] = Field(
        default_factory=dict,
        description="Custom kwargs to pass to LLM completion",
    )

class OpenAIConfig(BaseConfig):
    model: str = "gpt-4o-mini"
    temperature: float = 0.0
    max_completion_tokens: int = 1000
    top_p: float = 0.3


class Config(BaseModel):
    openai: OpenAIConfig = OpenAIConfig()


def get_config() -> Config:
    return Config()
