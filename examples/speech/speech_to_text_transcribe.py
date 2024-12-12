from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

client = KrutrimCloud()

# Define request params for the speech_to_text API
audio_file_path = Path("../resources/speech_1.mp3")   # Adjust this path to the actual audio file
input_language = "eng"

try:

    with open(audio_file_path, 'rb') as audio_file:
        # Send the request to the API for speech-to-text translation
        response = client.languagelabs.transcribe.upload(
            file=audio_file,  # Now passing the file as a binary stream
            lang_code=input_language,
        )


    transcription_text = " ".join(response.data.text)

    # Print the transcription result
    print(f"Transcription Result: {transcription_text}")

    # Step 4: Save the extracted text to a file
    #save_extracted_text(transcription_output_path, transcription_text)
    response.save(output_dirpath="./output")

except Exception as e:
    # Catch any exceptions and print detailed error
    print("An error occurred while processing the request:",e)

