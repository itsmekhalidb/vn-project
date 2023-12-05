from openai import OpenAI
import os
import sys
import pandas as pd
import time
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY,
    )

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion)