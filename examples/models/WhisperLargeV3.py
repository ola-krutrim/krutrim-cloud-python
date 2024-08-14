from krutrim_cloud import KrutrimCloud
from krutrim_cloud.lib.utils import convert_audio_file_to_base64
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud()

audio_file_path = "../resources/hindi_sample.mp3"

audio_data = convert_audio_file_to_base64(audio_file_path)

try:
    print("Translate:")
    response = client.audio.translations.create(model_name="openai/whisper-large-v3", file=audio_data, task="translate")

    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

    print("*" * 100)

    print("Transcribe:")
    response = client.audio.transcriptions.create(
        model_name="openai/whisper-large-v3", file=audio_data, task="transcribe"
    )
    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

except Exception as exc:
    print(f"Exception: {exc}")
