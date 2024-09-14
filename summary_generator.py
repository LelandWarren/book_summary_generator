# main.py
import os
from openai_module.openai_summary import get_summary_openai
from transformers_module.transformers_summary import get_summary_transformers

# Define configuration for model usage (switch between 'openai' and 'transformers')
MODE = "transformers"  # Change to "openai" to use OpenAI API

def get_book_summary(book_title):
    if MODE == "openai":
        return get_summary_openai(book_title)
    elif MODE == "transformers":
        return get_summary_transformers(book_title)
    else:
        raise ValueError("Invalid mode selected. Choose either 'openai' or 'transformers'.")

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
    book_title = "The Great Gatsby"  # Replace with your book title
    generate_book_summary(book_title)
