import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

from helper.write_to_css_file import write_to_css_file

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

# I like to use three double quotation marks for my prompts because it's easier to read
prompt = """Generate media queries for CSS data with breakpoints at 375px, 480px, 620px, 768px, 990px, 1200px, 1400px, 1600px, and 1920px.\n.heading_element_top_hero {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 42px;
    line-height: 60px;
    letter-spacing: 0.21px;
    color: #0E101A;
    max-width: 375px;
    width: 100%;
} ###
        """
def calculate_byte_size(text):
    return len(text.encode('utf-8'))

token_size = calculate_byte_size(prompt)

print(token_size)

llm = OpenAI(
    model_name=os.getenv("model_id"),
    openai_api_key=os.getenv("API_KEY"),
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    max_tokens=2048 - token_size,
    model_kwargs={'stop': 'END'}
)

completion = llm(prompt)
write_to_css_file(completion, 'test.css')
print(completion)

# def generate_completion(prompt):
#     response = openai.Completion.create(
#         model="curie:ft-personal:breakpoint-model-2-2023-05-22-08-19-28",
#         prompt=prompt,
#         temperature=1,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         stop=["END"]
#     )

#     return response.choices[0].text.strip()

# # Usage
# result = generate_completion(prompt=prompt)
# print(result)
