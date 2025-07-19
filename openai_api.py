# openai_api.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_interview_response(prompt, model="gpt-4", temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an AI interview assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"
