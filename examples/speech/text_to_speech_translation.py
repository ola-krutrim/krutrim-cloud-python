from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from krutrim_cloud.lib.utils import save_audio_file

# Load environment variables
load_dotenv()

# Initialize KrutrimCloud client
client = KrutrimCloud()

# Define request params for the text_to_speech_translation API
input_text = "Who are you and how are you doing?"
src_lang_code = "eng"  # Source language (English)
tgt_lang_code = "hin"  # Target language (Hindi)
input_speaker = "male"  # Speaker type


# Main script to call the text_to_speech_translation API and save the audio file
try:
    # Step 1: Call the text_to_speech_translation API to process the input text
    response = client.languagelabs.tts_trans.run(
        input_text=input_text,
        src_lang_code=src_lang_code,
        tgt_lang_code=tgt_lang_code,
        input_speaker=input_speaker
    )

    # Step 2 : extract the audio file URL
    audio_file_download_url = response.data.audio_file
    print(f"Audio file available at: {audio_file_download_url}")

    # Step 3: Save the audio file using the save function
    save_audio_file(audio_file_download_url, output_dirpath="./output", filename="output.mp3")


except Exception as exc:
    print(f"Exception: {exc}")
