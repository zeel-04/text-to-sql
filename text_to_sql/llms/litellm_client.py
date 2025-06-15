from litellm import acompletion
from litellm.utils import get_valid_models
from tenacity import retry, stop_after_attempt

from config.settings import LLMSettings
from text_to_sql.llms.base import BaseLLM, Message, T


class LiteLLM(BaseLLM):
    """LiteLLM implementation of the BaseLLM class."""

    def __init__(self, config: LLMSettings):
        """Initialize LiteLLM client with configuration.

        Args:
            config: LLM settings configuration
        """
        self.config = config

    @retry(stop=stop_after_attempt(3))
    async def generate_text(
        self,
        messages: list[Message],
        model: str | None = None,
        temperature: float | None = None,
        max_completion_tokens: int | None = None,
        top_p: float | None = None,
        **kwargs: dict,
    ) -> str:
        """Generate plain text response."""
        response = await acompletion(
            model=model or self.config.model,
            messages=messages,
            temperature=temperature or self.config.temperature,
            max_completion_tokens=max_completion_tokens
            or self.config.max_completion_tokens,
            top_p=top_p or self.config.top_p,
            api_key=self.config.api_key,
            **kwargs,
        )
        return response.choices[0].message.content

    @retry(stop=stop_after_attempt(3))
    async def generate_text_with_response_format(
        self,
        messages: list[Message],
        response_format: type[T],
        model: str | None = None,
        temperature: float | None = None,
        max_completion_tokens: int | None = None,
        top_p: float | None = None,
        **kwargs: dict,
    ) -> T:
        """Generate response with a response format."""
        response = await acompletion(
            model=model or self.config.model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=temperature or self.config.temperature,
            max_completion_tokens=max_completion_tokens
            or self.config.max_completion_tokens,
            top_p=top_p or self.config.top_p,
            api_key=self.config.api_key,
            **kwargs,
        )
        response_content = response.choices[0].message.content
        return response_format.model_validate_json(response_content)

    async def get_available_models(self) -> list[str]:
        """Get a list of available models."""
        return get_valid_models(check_provider_endpoint=True)
