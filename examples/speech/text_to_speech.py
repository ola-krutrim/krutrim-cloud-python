from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from krutrim_cloud.lib.utils import save_audio_file

# Load environment variables
load_dotenv()

# Initialize KrutrimCloud client
client = KrutrimCloud()

# Define request params for the text_to_speech API
input_text = "Major exports include petroleum products, textile goods, jewellery, software, engineering goods, chemicals, and manufactured leather goods."
input_language = "eng"
input_speaker = "male"

# Main script to call the API and save the audio file
try:
    # Step 1: Call the text_to_speech API to process the input text
    response = client.languagelabs.tts.run(
        input_text=input_text,
        input_language=input_language,
        input_speaker=input_speaker
    )

    #Step 2 : extract the audio file URL
    audio_file_download_url = response.data.audio_file
    print(f"Audio file available at: {audio_file_download_url}")

    # Step 3 : save the audio file
    save_audio_file(audio_file_download_url, output_dirpath="./output", filename="output.mp3")

except Exception as exc:
    print(f"Exception: {exc}")
