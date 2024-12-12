from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the KrutrimCloud client
client = KrutrimCloud()

# Set the text for summarization
text = """
    Krutrim, a part of the Ola group, is working on creating the AI computing stack of the future.
    We endeavor to deliver a state-of-the-art AI computing stack that encompasses the AI computing infrastructure,
    AI Cloud, foundational models, and AI-powered end applications for the Indian market. Our envisioned AI computing
    stack can empower consumers, startups, enterprises and scientists across India and the world to build their end
    AI applications or AI models. While we are building foundational models across text, voice, and vision relevant to
    our focus markets, we are also developing AI training and inference platforms that enable AI research and development
    across industry domains. The platforms being built by Krutrim have the potential to impact millions of lives in India,
    across income and education strata, and across languages. The team at Krutrim represents a convergence of talent across
    AI research, Applied AI, Cloud Engineering, and semiconductor design. Our teams operate from three locations: Bangalore,
    Singapore & San Francisco.
"""

# Define the parameters for the summarization API
params = {
    "text": text,  # The input text to summarize
    "input_language": "eng",  # Language of the input text (English)
    "summary_size": 10  # Desired summary size (number of sentences/words)
}

try:
    # Call the summarization API
    response = client.languagelabs.summarization.run(**params)

    summary_text = response.data.get("summaryText", "No summary text available")
    print(f"Summary: {summary_text}")

    # Store generated output in local storage
    response.save(output_dirpath="./output")

except Exception as exc:
    print(f"Exception: {exc}")
