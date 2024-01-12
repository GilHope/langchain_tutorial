# Output Parsers

# Let's start with defining how we would like the LLM output to look like:

import os
import openai
import datetime
import json
from langchain_community.chat_models import ChatOpenAI  # Corrected import
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv

# Load OpenAI API key
_ = load_dotenv(find_dotenv())  # read local .env file
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

# Review template
review_template = """\
For the following text, extract the following information:
gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.
delivery_days: How many days did it take for the product \
to arrive? If this information is not found, output -1.
price_value: Extract any sentences about the value or price, \
and output them as a comma separated Python list.
Format the output as JSON with the following keys:
gift, delivery_days, price_value
text: {text}
"""

# Create prompt template
prompt_template = ChatPromptTemplate.from_template(review_template)

# Customer review
customer_review = """\
This leaf blower is pretty amazing. It has four settings: \
candle blower, gentle breeze, windy city, and tornado. \
It arrived in two days, just in time for my wife's \
anniversary present. \
I think my wife liked it so much she was speechless. \
So far I've been the only one using it, and I've been \
using it every other morning to clear the leaves on our lawn. \
It's slightly more expensive than the other leaf blowers \
out there, but I think it's worth it for the extra features.
"""

# Format messages
messages = prompt_template.format_messages(text=customer_review)

# Invoke ChatOpenAI
response = chat.invoke(messages)

# Print and analyze the response
print(response.content)

# Attempt to parse the response as JSON
try:
    parsed_response = json.loads(response.content)
    print("Parsed JSON:", parsed_response)
except json.JSONDecodeError:
    print("Failed to decode response as JSON.")
