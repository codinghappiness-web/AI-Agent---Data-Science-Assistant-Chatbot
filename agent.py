from openai import OpenAI
from prompts import BASE_PROMPT
from utils import get_api_key

client = OpenAI(api_key=get_api_key())

class DataScienceAssistant:
    def ask(self, question):
        prompt = BASE_PROMPT.format(question=question)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You're an expert data science tutor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
