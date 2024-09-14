import openai
import os
from dotenv import load_dotenv


model = "gpt-3.5-turbo"

# Load OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get overall book summary using the new OpenAI completions API
def get_book_summary(book_title):
    prompt = f"Write an in-depth summary of the book '{book_title}'. Format it as Overview, Key Themes, Key Quotes and Insights, Why This Book Matters, and Conclusion."
    
    # Using the new `openai.completions.create` API with the correct parameters
    response = openai.completions.create(
        model=model,
        prompt=prompt,
        max_tokens=2000
    )
    
    return response['completion']

# Function to save the summary as markdown
def save_summary_as_markdown(book_title, summary):
    folder_path = f"./books/{book_title}"
    os.makedirs(folder_path, exist_ok=True)
    with open(f"{folder_path}/summary.md", 'w') as file:
        file.write(summary)

# Main function to generate and save the book summary
def generate_book_summary(book_title):
    summary = get_book_summary(book_title)
    save_summary_as_markdown(book_title, summary)
    print(f"Summary for '{book_title}' saved as summary.md.")

# Example usage
if __name__ == "__main__":
    book_title = "Sample Book"  # Replace with your book title
    generate_book_summary(book_title)
