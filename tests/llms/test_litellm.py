import pytest
from pydantic import BaseModel

from config.settings import get_settings
from text_to_sql.llms.litellm_client import LiteLLM

config = get_settings()

class DemoResponse(BaseModel):
    name: str
    age: int


@pytest.fixture
def message():
    return [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is the capital of France?"},
    ]

@pytest.fixture
def message_with_response_format():
    return [
        {"role": "system", "content": "You are a helpful assistant.answer in json format. with keys name and age"},
        {"role": "user", "content": "I am 25 years old and my name is John"},
    ]

def test_litellm_object_creation():
    llm = LiteLLM(config.openai)
    assert llm is not None


@pytest.mark.asyncio
async def test_response(message):
    llm = LiteLLM(config.openai)
    response = await llm.generate_text(message)
    assert response is not None and response != "" and isinstance(response, str)


@pytest.mark.asyncio
async def test_response_with_response_format(message_with_response_format):
    llm = LiteLLM(config.openai)
    response = await llm.generate_text_with_response_format(message_with_response_format, response_format=DemoResponse)
    assert response is not None and isinstance(response, DemoResponse)
