from abc import ABC, abstractmethod

from .schemas import Message, T


class BaseLLM(ABC):
    """Base class for all LLM implementations."""

    @abstractmethod
    async def generate_text(
        self,
        messages: list[Message],
        model: str,
        temperature: float,
        max_completion_tokens: int,
        top_p: float,
        **kwargs: dict,
    ) -> str:
        """Generate text response from a list of messages."""
        pass

    @abstractmethod
    async def generate_text_with_response_format(
        self,
        messages: list[Message],
        model: str,
        response_format: type[T],
        temperature: float,
        max_completion_tokens: int,
        top_p: float,
        **kwargs: dict,
    ) -> T:
        """Generate structured response using Pydantic model format."""
        pass

    @abstractmethod
    async def get_available_models(self) -> list[str]:
        """Get a list of available models."""
        pass
