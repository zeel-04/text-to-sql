from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """Base config for LLM configurations."""

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


class OpenAILLMConfig(LLMConfig):
    """Config for OpenAI LLM."""

    model: str = "gpt-4o-mini"
    temperature: float = 0.0
    max_completion_tokens: int = 1000
    top_p: float = 1.0


print(OpenAILLMConfig().model_dump())
