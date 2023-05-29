import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

chat = ChatOpenAI(temperature=1.0, openai_api_key=os.getenv("API_KEY"), model_name='gpt-3.5-turbo')

def chat_with_gpt(messages):
    response = chat(messages)
    return response.content

def get_completion_langchain(css):
    template1 = f"""Generate given CSS data to Breakpoints 480, 620, 990, 1190, and 1440 pixels wide to make the website responsive. And provide only CSS rules only. Don't include any comments or additional text. {css}"""
    
    messages = [SystemMessage(content="You are a helpful assistant for generating HTML and CSS code.")]

    messages.append(HumanMessage(content=template1))
    ai_response_css = chat_with_gpt(messages)
    messages.append(AIMessage(content= ai_response_css))

    return ai_response_css


# html_tags = "<div><p>Hello, world!</p></div>"
# css = "div { position: absolute; }"
# for i in range(10):
#     html_result, css_result = get_completion_langchain(html_tags, css)
#     print("Generated HTML:", html_result)
#     print("Generated CSS:", css_result)
#     print("range", i)
