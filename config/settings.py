import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

# Load environment variables
load_dotenv()


class LLMSettings(BaseSettings):
    """Base settings for LLM configurations."""

    api_key: str | None = Field(None, description="API key for the LLM service")
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

    api_key: str = os.getenv("OPENAI_API_KEY")
    model: str = "gpt-4.1"


class Settings(BaseSettings):
    """Main application settings."""

    openai: OpenAISettings = OpenAISettings()


def get_settings() -> Settings:
    """Get settings instance. Use this instead of a global variable."""
    return Settings()


settings = get_settings()

if __name__ == "__main__":
    test_settings = get_settings()
    api_key = test_settings.openai.api_key
    print(f"API key loaded: {'✓' if api_key else '✗'}")
    print(f"API key prefix: {api_key[:7]}..." if api_key else "No API key found")
