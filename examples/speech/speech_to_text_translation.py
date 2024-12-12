from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables (e.g., API_KEY)
load_dotenv()

# Initialize KrutrimCloud client with the API key (if required by the API)
client = KrutrimCloud()

# Define request parameters for the speech_to_text_translation API
audio_file_path = Path("../resources/speech_1.mp3")   # Adjust this path to the actual audio file
src_language = "eng"  # Source language (e.g., English)
tgt_language = "hin"  # Target language (e.g., Hindi)

try:

    # Open the audio file and read it as bytes (file-like object)
    with open(audio_file_path, 'rb') as audio_file:
        # Send the request to the API for speech-to-text translation
        response = client.languagelabs.stt_trans.upload(
            file=audio_file,  # Pass the file as a file-like object
            src_lang_code=src_language,
            tgt_lang_code=tgt_language
        )

    translated_text = response.data.translated_text

    print(f"Translated Text: {translated_text}")

    #Save the extracted text to a file
    response.save(output_dirpath="./output")

except Exception as e:
    # Catch any exceptions and print detailed error
    print("An error occurred while processing the request:",e)

