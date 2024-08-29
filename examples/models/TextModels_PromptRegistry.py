from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from krutrim_cloud.lib.prompt_registry import PromptRegistry, Category

load_dotenv()

client = KrutrimCloud()
registry = PromptRegistry()

# Print out the list of categories of prompts
print(f"List of Categories of Prompts: {registry.list_categories()}")
print("*" * 100)

# Fetch the prompt based on chosen category
print(f"Prompt: {registry.get_prompt(Category.CREATIVE_WRITING)}")
print("*" * 100)

# Search from the prompt registry based on the keyword
print(f"Searched Prompt: {registry.search_prompts('PRD')}")
print("*" * 100)

# Update the prompt of a specific category
registry.update_prompt(Category.CREATIVE_WRITING, prompt="<This is my customized prompt>")

# Save the prompts into the given filepath
registry.save_prompts_to_file("./my_prompts.json")

# Load the prompts from the given filepath
registry.load_prompts_from_file("./my_prompts.json")

messages = [
    {"role": "system", "content": "You are a product manager."},
    {
        "role": "user",
        "content": registry.get_prompt(Category.PRODUCT_DEVELOPMENT),
    },
]

model_name = "Mistral-7B-Instruct"
# model_name = "Meta-Llama-3-8B-Instruct"
# model_name = "Krutrim-spectre-v2"
try:
    response = client.chat.completions.create(
        model=model_name, messages=messages, max_tokens=4096
    )  # Use max_tokens=2048 for Krutrim-spectre-v2 model as it has less token length

    # Access generated output
    txt_output_data = response.choices[0].message.content  # type:ignore
    print(f"Output: \n{txt_output_data}")

    # OR
    # Save generated output
    response.save(output_dirpath="./output")
except Exception as exc:
    print(f"Exception: {exc}")
