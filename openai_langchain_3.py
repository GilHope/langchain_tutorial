import os
import openai
import datetime
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

# Load OpenAI API key
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Define the model based on the current date
current_date = datetime.datetime.now().date()
target_date = datetime.date(2024, 6, 12)

if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

# Initialize LangChain Chat Model
chat = ChatOpenAI(temperature=0.0, model=llm_model)

# def get_completion(prompt, model=llm_model):
#     try:
#         messages = [{"role": "user", "content": prompt}]
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=messages,
#             temperature=0, 
#         )
#         return response.choices[0].message["content"]
#     except Exception as e:
#         print(f"An error occurred: {e}")

# Prompt template
template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```"""

prompt_template = ChatPromptTemplate.from_template(template_string)

# Customer style and message
customer_style = """American English \
in a calm and respectful tone"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

# Format customer message
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

# Call the LLM to translate to the style of the customer message
customer_response = chat(customer_messages)
print(customer_response.content)

# Service reply and style
service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!"""

service_style_pirate = """\
a polite tone \
that speaks in English Pirate"""

# Format service message
service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

# Translate service message
service_response = chat(service_messages)
print(service_response.content)