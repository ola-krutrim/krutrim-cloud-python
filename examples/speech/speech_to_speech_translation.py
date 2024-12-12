from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from pathlib import Path
import traceback
from krutrim_cloud.lib.utils import save_audio_file

# Load environment variables (e.g., API_KEY)
load_dotenv()

# Initialize KrutrimCloud client with the API key
client = KrutrimCloud()

# Define request parameters for the speech_to_speech_translation API
audio_file_path = Path("../resources/speech_1.mp3")  # Adjust this path to the actual audio file
src_language = "eng"  # Source language (e.g., English)
tgt_language = "hin"  # Target language (e.g., Hindi)
input_speaker = "male"  # Source speaker (e.g., "male" or "female")


try:

    with open(audio_file_path, 'rb') as audio_file:
        # Send the request to the API for speech-to-text translation
        response = client.languagelabs.sts_trans.upload(
            file=audio_file,
            src_lang_code=src_language,
            tgt_lang_code=tgt_language,
            input_speaker=input_speaker
        )


    # Extract the URL for downloading the translated audio file
    audio_file_download_url = response.data.audio_file

    # Print the download URL for the translated audio file
    print(f"Audio file available for download at: {audio_file_download_url}")

    # save audio file
    save_audio_file(audio_file_download_url, output_dirpath="./output", filename="output.mp3")


except Exception as e:
    # Catch any exceptions and print detailed error
    print("An error occurred while processing the request:",e)

