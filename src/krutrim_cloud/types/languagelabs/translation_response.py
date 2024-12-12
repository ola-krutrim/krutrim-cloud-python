import os
from typing import Dict
from ..._models import BaseModel
from ...lib.utils import get_current_time_string

__all__ = ["TranslationResponse"]

class TranslationResponse(BaseModel):
    status: str
    data: Dict[str, str]
    http_status: str
    timestamp: int
    code: int

    def save(self, output_dirpath: str, filename: str = ""):
        """
        Saves the translated text to a text file.
        """
        try:

            # Create the directory if it does not exist
            os.makedirs(output_dirpath, exist_ok=True)

            if not filename:
                filename = f"translation_result-{get_current_time_string()}.txt"

            with open(f"{output_dirpath}/{filename}", "w") as file:
                # file.write(f"Translation Result (Timestamp: {self.timestamp}):\n")
                file.write(f"Translated Text: {self.data.get('translated_text')}\n")

            print(f"Results saved to {output_dirpath}/{filename}")
        except Exception as exc:
            print(f"Error saving results: {exc}")
