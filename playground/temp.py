import asyncio
from text_to_sql.llms.config import get_config, BaseConfig
from text_to_sql.llms.litellm_client import LiteLLM
from tests.llms.test_litellm import DemoResponse

config = get_config()

new_config = BaseConfig(model="gpt-4o-mini", temperature=0.0, max_completion_tokens=1000, top_p=1.0)
llm = LiteLLM(new_config)

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