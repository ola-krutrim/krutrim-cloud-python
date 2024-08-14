from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": "Give a random number.  Provide only number without any explatation, for example: \nRandom Number: <number>",
    },
]
model_name = "Mistral-7B-Instruct"
# model_name = "Meta-Llama-3-8B-Instruct"
# model_name = "Krutrim-spectre-v2"
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
