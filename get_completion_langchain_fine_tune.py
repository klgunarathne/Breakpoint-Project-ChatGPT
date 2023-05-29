import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

chat = ChatOpenAI(temperature=1.0, openai_api_key=os.getenv(
    "API_KEY"), model_name=os.getenv("model_id"))


def calculate_byte_size(text):
    return len(text.encode('utf-8'))


def chat_with_gpt(messages):
    response = chat(messages)
    return response.content


def get_completion_langchain_fine_tune(css):
    template1 = f"""Generate media queries for CSS data with breakpoints at 375px, 480px, 620px, 768px, 990px, 1200px, 1400px, 1600px, and 1920px.\n{css} ###"""

    token_size = calculate_byte_size(template1)

    llm = OpenAI(
        model_name=os.getenv("model_id"),
        openai_api_key=os.getenv("API_KEY"),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=2048 - token_size,
        model_kwargs={'stop': 'END'}
    )

    ai_response_css = llm(template1)

    return ai_response_css