# openai_module/openai_summary.py
import openai
import os
from dotenv import load_dotenv

# Load OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_summary_openai(book_title):
    prompt = f"Write an in-depth summary of the book '{book_title}'. Format it as Overview, Key Themes, Key Quotes and Insights, Why This Book Matters, and Conclusion."
    
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Use gpt-4 if you have access
        prompt=prompt,
        max_tokens=500
    )
    
    return response['choices'][0]['text']
