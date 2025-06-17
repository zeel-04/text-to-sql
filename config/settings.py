from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

# Load environment variables
load_dotenv()


class LLMSettings(BaseSettings):
    """Base settings for LLM configurations."""

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


class OpenAISettings(LLMSettings):
    """OpenAI-specific settings."""

    model: str = "gpt-4.1"


class Settings(BaseSettings):
    """Main application settings."""

    openai: OpenAISettings = OpenAISettings()


def get_settings() -> Settings:
    """Get settings instance. Use this instead of a global variable."""
    return Settings()


settings = get_settings()


