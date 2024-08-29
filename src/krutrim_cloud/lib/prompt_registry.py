from enum import Enum
import json
import os
from krutrim_cloud.lib.prompts import prompts
from pathlib import Path
from typing import Dict


class Category(Enum):
    """Enumeration for prompt categories."""

    CREATIVE_WRITING = "Creative Writing"
    CUSTOMER_SUPPORT = "Customer Support"
    TECHNICAL_SUPPORT = "Technical Support"
    MARKETING_AND_SALES = "Marketing and Sales"
    PRODUCT_DEVELOPMENT = "Product Development"
    EDUCATION_AND_TRAINING = "Education and Training"
    RESEARCH_AND_ANALYSIS = "Research and Analysis"
    SOCIAL_MEDIA_MANAGEMENT = "Social Media Management"
    HEALTH_AND_WELLNESS = "Health and Wellness"
    LEGAL_AND_COMPLIANCE = "Legal and Compliance"
    HUMAN_RESOURCES = "Human Resources"
    FINANCE_AND_ACCOUNTING = "Finance and Accounting"
    SOFTWARE_DEVELOPMENT = "Software Development"
    GAMING_AND_ENTERTAINMENT = "Gaming and Entertainment"
    GENERAL_KNOWLEDGE = "General Knowledge"


class PromptRegistryError(Exception):
    """Custom exception for PromptRegistry errors."""

    pass


class PromptRegistry:
    def __init__(self) -> None:
        self.registry: Dict[str, str] = {}
        try:
            self.load_prompts()
        except Exception as e:
            raise PromptRegistryError(f"Failed to load default prompts: {e}")

    def load_prompts(self):
        """Load default prompts."""
        self.registry = prompts

    def load_prompts_from_file(self, filepath: str):
        """Load prompts from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Prompt file '{filepath}' not found.")
        else:
            try:
                with open(filepath, "r") as file:
                    self.registry = json.load(file)
            except json.JSONDecodeError as e:
                raise PromptRegistryError(f"Error decoding JSON from '{filepath}': {e}")
            except Exception as e:
                raise PromptRegistryError(f"An error occurred while loading prompts from '{filepath}': {e}")

    def save_prompts_to_file(self, output_filepath: str):
        """Save prompts to a JSON file."""
        try:
            Path.mkdir(Path(output_filepath).parent, exist_ok=True)
            with open(output_filepath, "w") as file:
                json.dump(self.registry, file, indent=4)
        except Exception as e:
            raise PromptRegistryError(f"Failed to save prompts to '{output_filepath}': {e}")

    def get_prompt(self, category: Category):
        """Retrieve the prompt under a specific category."""
        try:
            return self.registry[category.value]
        except KeyError:
            raise PromptRegistryError(f"Category '{category.value}' not found in the registry.")

    def list_categories(self):
        """List all available categories."""
        try:
            return [category.name for category in Category]
        except Exception as e:
            raise PromptRegistryError(f"An error occurred while listing categories: {e}")

    def update_prompt(self, category: Category, prompt: str, output_filepath: str = ""):
        """Update the prompt of a specific category."""
        try:
            self.registry[category.value] = prompt
            if output_filepath:
                self.save_prompts_to_file(output_filepath)
        except Exception as e:
            raise PromptRegistryError(f"Failed to update prompt for category '{category.value}': {e}")

    def search_prompts(self, keyword: str):
        """Search for prompts containing a specific keyword."""
        try:
            """Search for prompts containing a specific keyword."""
            results = {
                category: prompt for category, prompt in self.registry.items() if keyword.lower() in prompt.lower()
            }
            return results
        except Exception as e:
            raise PromptRegistryError(f"An error occurred while searching for prompts with keyword '{keyword}': {e}")
