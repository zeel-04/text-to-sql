from litellm import acompletion
from litellm.utils import get_valid_models
from tenacity import retry, stop_after_attempt

from .base import BaseLLM, T
from .config import BaseConfig
from .schemas import Message


class LiteLLM(BaseLLM):
    """LiteLLM implementation of the BaseLLM class."""

    def __init__(self, config: BaseConfig):
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
        response = await acompletion(
            model=model or self.config.model,
            messages=messages,
            temperature=temperature or self.config.temperature,
            max_completion_tokens=max_completion_tokens
            or self.config.max_completion_tokens,
            top_p=top_p or self.config.top_p,
            **self.config.custom_kwargs,
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
        """Generate response with a structured output."""
        response = await acompletion(
            model=model or self.config.model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=temperature or self.config.temperature,
            max_completion_tokens=max_completion_tokens
            or self.config.max_completion_tokens,
            top_p=top_p or self.config.top_p,
            **self.config.custom_kwargs,
            **kwargs,
        )
        response_content = response.choices[0].message.content
        return response_format.model_validate_json(response_content)

    async def get_available_models(self) -> list[str]:
        """Get a list of available models."""
        return get_valid_models(check_provider_endpoint=True)
