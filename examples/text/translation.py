from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the KrutrimCloud client
client = KrutrimCloud()

# Set the text for translation
text = """
    Krutrim, a part of the Ola group, is working on creating the AI computing stack of the future.
    We endeavor to deliver a state-of-the-art AI computing stack that encompasses the AI computing infrastructure,
    AI Cloud, foundational models, and AI-powered end applications for the Indian market.
"""

# Define the parameters for the translation API
params = {
    "text": text,  # The text to translate
    "src_language": "eng_Latn",  # Source language (English)
    "tgt_language": "hin_Deva",  # Target language (Hindi in Devanagari script)
    "model": "krutrim-translate-v1.0"  # Translation model
}

try:
    # Call the translation API
    response = client.languagelabs.translation.run(**params)

    # Access the translated text from the response data dictionary
    translated_text = response.data.get("translated_text", "No translation available")
    print(f"Translated Text: {translated_text}")

    # Store generated output in local storage
    response.save(output_dirpath="./output")

except Exception as exc:
    print(f"Exception: {exc}")
