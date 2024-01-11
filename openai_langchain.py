# Chat API : OpenAI

# Let's start with a direct API calls to OpenAI.


import os
import openai
from dotenv import load_dotenv
import datetime

load_dotenv()

# Set the OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')



# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the llm_model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


# Test the get_completion function
result = get_completion("What is 1+1?")
print(result)
