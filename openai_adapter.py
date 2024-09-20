from openai import OpenAI
import os
from dotenv import load_dotenv

class OpenAIAdapter():
    def __init__(self):
        load_dotenv('.env')
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.system_prompt = self.read_file("system_prompt.txt")

    def read_file(self, name):
        with open(name, "r", encoding="utf-8") as f:
            text = f.read()
        return text

    def create_chat(self, question):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {'role': 'system', 'content': self.system_prompt},
                {'role': 'user', 'content': question}
            ]
        )
        chat_response = response.choices[0].message.content.strip()
        return chat_response
    
if __name__ == "__main__":
    Aqua = OpenAIAdapter()
    message = Aqua.create_chat("こんにちは")
    print(message)
