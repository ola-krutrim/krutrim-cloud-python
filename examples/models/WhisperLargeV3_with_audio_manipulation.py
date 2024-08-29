from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from pydub import AudioSegment  # type: ignore

load_dotenv()

client = KrutrimCloud()

try:

    # Audio Manipulation supported by pydub
    from pathlib import Path

    audio_data_1 = AudioSegment.from_file(  # type: ignore
        Path("<path of first file>")
    )  # for any duration of audio/video files

    audio_data_2 = AudioSegment.from_file(  # type: ignore
        Path("<path of second file>")
    )  # for any duration of audio/video files

    # Slice and Concatenate the audio data in milliseconds
    # All files must be in same audio language to get desired results of translation/transcription
    final_data = (  # type: ignore
        audio_data_1[: 10 * 1000] + audio_data_2[10 * 1000 : 20 * 1000] + audio_data_2[-5 * 1000 :]
    )  # first 10 seconds of first file + 10 seconds (10 to 20) of second file + last 5 seconds of second file

    # Export the audio for validation purposes
    final_data.export("./tmp_audio.mp3", format="mp3")  # type: ignore
    print("Translate:")
    response = client.audio.translations.create(model_name="openai/whisper-large-v3", file=final_data, task="translate")  # type: ignore

    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

    print("*" * 100)

    print("Transcribe:")
    response = client.audio.transcriptions.create(
        model_name="openai/whisper-large-v3", file=final_data, task="transcribe"  # type: ignore
    )
    # Access generated output
    print(f"Output: {response.predictions}")
    # OR
    # Save generated output
    response.save("./output")

except Exception as exc:
    print(f"Exception: {exc}")
