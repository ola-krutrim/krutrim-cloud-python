from krutrim_cloud import KrutrimCloud
from krutrim_cloud.lib.utils import convert_audio_file_to_base64
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

client = KrutrimCloud()

try:
    # Send the base64 encoded audio data (Less than 2 minutes audio duration)
    # audio_file_path = "../resources/hindi_sample.mp3"
    # data = convert_audio_file_to_base64(audio_file_path)

    # OR
    # Send the Path object of the Audio or Video file from local storage (Video only supported as Path object, not base64 encoded string)
    data = Path("../resources/hindi_sample.mp3")  # for any duration of audio/video files

    print("Translate:")
    response = client.audio.translations.create(model_name="openai/whisper-large-v3", file=data, task="translate")

    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

    print("*" * 100)

    print("Transcribe:")
    response = client.audio.transcriptions.create(model_name="openai/whisper-large-v3", file=data, task="transcribe")
    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

except Exception as exc:
    print(f"Exception: {exc}")
