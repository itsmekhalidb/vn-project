import openai
import os
import sys
import pandas as pd
import time

class AiTest():
    openai.api_key = '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'

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

def main(args):
    test = AiTest()
    print(test.get_completion("hi, how are you?"))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))