# Author: ray
# Date: 9/16/23
# Description:

import os
import openai
from dotenv import load_dotenv
# print(f"checking api: {os.getenv('OPENAI_API_KEY')}")


# Load .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(role_description: str, prompt: str):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": role_description},
        {"role": "user", "content": prompt}
      ]
    )

    return completion.choices[0].message