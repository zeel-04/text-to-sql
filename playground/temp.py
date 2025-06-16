import asyncio
from config.settings import get_settings
from text_to_sql.llms.litellm_client import LiteLLM
from text_to_sql.llms.response_models import DemoResponse

config = get_settings()

llm = LiteLLM(config.openai)

async def main():
    response = await llm.generate_text_with_response_format(
        messages=[
            {"role": "system", "content": "You are a helpful assistant..answer in json format. with keys name and age"},
            {"role": "user", "content": "I am 25 years old. My name is John"},
        ],
        response_format=DemoResponse,
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())