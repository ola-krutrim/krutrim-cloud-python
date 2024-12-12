from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the KrutrimCloud client
client = KrutrimCloud()

# Set the text for entity extraction in Hindi
text = """
    मेरे मित्र राजेश कुमार, जिनका जन्म 5 मई 1985 को दिल्ली में हुआ था, अब बेंगलुरु में रहते हैं। उन्होंने
    2010 में आईआईटी दिल्ली से कंप्यूटर विज्ञान में स्नातक की डिग्री प्राप्त की थी। राजेश
    की पत्नी का नाम अंजलि है और उनके दो बच्चे हैं। राजेश एक सॉफ्टवेयर इंजीनियर के रूप में
    इंफोसिस में काम करते हैं। उनका फोन नंबर 9876543210 है और उनका ईमेल पता
    rajesh.kumar@example.com है। राजेश का पता 123, एमजी रोड, बेंगलुरु - 560001 है।
"""

# Define the parameters for the entity extraction API
params = {
    "text": text,
    "param_list": ["ner", "pii"],  # We want both NER and PII extractions
    "lang_from": "hin"  # Language is Hindi
}

try:
    # Call the entity_extraction API
    response = client.languagelabs.entity_extraction.run(**params)

    # Iterate through the response data to print extracted entities
    for entity in response.data:
        # Access properties of the 'EntityExtractionData' object using dot notation
        print(f"\nTitle: {entity.title} (Color: {entity.color})")

        # Iterate through the entities in each category
        for entry in entity.data:
            # Access properties of the 'EntityExtractionItem' object using dot notation
            print(f"{entry.label}: {entry.value}")

    print(f"\nTotal Entities Extracted: {response.Total_entities}")

    # Store generated output in local storage
    response.save(output_dirpath="./output")


except Exception as exc:
    print(f"Exception: {exc}")
