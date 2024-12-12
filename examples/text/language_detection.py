from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud()

# Set the text for language detection
query = "Hey there, welcome to Language Labs,ಎಲ್ಲವೂ ಚೆನ್ನಾಗಿದೆ"

try:
    # Call the language detection API correctly
    response = client.languagelabs.language_detection.run(
        query=query
    )

    # response.data is a list of objects with 'label' and 'value' attributes
    for entry in response.data:
        # Access the 'label' and 'value' attributes of each entry (assuming they are attributes)
        print(f"{entry.label}: {entry.value}")

    # Store generated output in local storage
    response.save(output_dirpath="./output")

except Exception as exc:
    print(f"Exception: {exc}")
