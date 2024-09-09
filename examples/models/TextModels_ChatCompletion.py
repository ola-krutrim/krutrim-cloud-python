from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud()

model_name = "Mistral-7B-Instruct"
# model_name = "Meta-Llama-3-8B-Instruct"
# model_name = "Krutrim-spectre-v2"
# model_name = "Gemma-2-27B-IT"
# model_name = "Reflection-Llama-3.1-70B"

# Notes:
# Use this system message for "Reflection-Llama-3.1-70B" for better performance
# "You are an AI system, capable of reasoning and reflection. Reason through the query inside <thinking> tags, and then provide your final response inside <output> tags. If you make a mistake, correct yourself inside <reflection> tags"

# For Gemma model, don't provide the system message as it doesn't support the system prompts

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "Give a random number.  Provide only number without any explatation, for example: \nRandom Number: <number>",
    },
]

try:
    response = client.chat.completions.create(model=model_name, messages=messages)

    # Access generated output
    txt_output_data = response.choices[0].message.content  # type:ignore
    print(f"Output: \n{txt_output_data}")

    # OR
    # Save generated output
    response.save(output_dirpath="./output")
except Exception as exc:
    print(f"Exception: {exc}")
