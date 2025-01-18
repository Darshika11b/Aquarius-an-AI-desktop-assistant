import openai
import os

# Set up your API key (Replace with your actual API key)
openai.api_key = "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"

def chat_with_ai(prompt):
    """
    Function to interact with OpenAI's GPT model.
    Args:
        prompt (str): The user input
    Returns:
        str: AI-generated response
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_ai(user_input)
    print("AI:", response)

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK resources
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    Args:
        text (str): User's input text
    Returns:
        str: Sentiment label (Positive, Negative, or Neutral)
    """
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] > 0.05:
        return "Positive 😊"
    elif sentiment['compound'] < -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Example usage
while True:
    user_text = input("Enter a message: ")
    if user_text.lower() == "exit":
        break
    print("Sentiment:", analyze_sentiment(user_text))

from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

def summarize_text(text, max_len=100, min_len=30):
    """
    Summarizes a long text into a concise version.
    Args:
        text (str): The input text
        max_len (int): Maximum summary length
        min_len (int): Minimum summary length
    Returns:
        str: Summarized text
    """
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = """Artificial intelligence is the simulation of human intelligence 
          processes by machines, especially computer systems. 
          These processes include learning, reasoning, and self-correction."""
print("Summary:", summarize_text(text))



def detect_unauthorized_access():
    """
    Checks for unauthorized users in the system.
    """
    users = os.popen("who").read()
    unauthorized_users = ["hacker123", "intruder"]

    for user in unauthorized_users:
        if user in users:
            return f"⚠️ ALERT! Unauthorized access detected: {user}"

    return "✅ No unauthorized access detected."

print(detect_unauthorized_access())
