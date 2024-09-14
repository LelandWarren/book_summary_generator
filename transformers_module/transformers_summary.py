# transformers_module/transformers_summary.py
from transformers import pipeline

def get_summary_transformers(book_title):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    prompt = f"Summarize the book '{book_title}'."
    summary = summarizer(prompt, max_length=150, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']
