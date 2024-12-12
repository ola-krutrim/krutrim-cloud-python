from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize the KrutrimCloud client with the API key (assuming the client supports it)
client = KrutrimCloud()

# Set the text for sentiment analysis
text = """
    He felt a surge of joy as he watched the sunrise, painting the sky with vibrant hues of orange and pink.
"""

# Define the parameters for the sentiment analysis API
params = {
    "text": text,  # The text to analyze
    "lang_from": "eng",  # Source language (English)
}

try:
    # Call the sentiment analysis API
    response = client.languagelabs.sentiment_analysis.run(**params)

    # Access sentiment analysis results
    for entry in response.Sentiment:
        sentence = entry.get("label", "").strip()  # Remove leading/trailing whitespace
        sentiments = ", ".join(entry.get("value", []))
        print(f"Sentence: {sentence}\nSentiment: {sentiments}\n")

    # Store generated output in local storage
    response.save(output_dirpath="./output")

except Exception as exc:
    print(f"Exception: {exc}")
