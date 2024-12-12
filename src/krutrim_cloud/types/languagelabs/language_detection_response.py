import os
from typing import List, Dict
from ..._models import BaseModel
from ...lib.utils import get_current_time_string

__all__ = ["LanguageDetectionResponse", "LanguageDetectionResult"]

class LanguageDetectionResult(BaseModel):
    label: str
    value: str

class LanguageDetectionResponse(BaseModel):
    status: str
    data: List[LanguageDetectionResult]

    def save(self, output_dirpath: str, filename: str = ""):
        """
        This method can be used to save the results into a file,such as a text file.
        If you don't want to save to a file, you can adjust it based on your requirements.
        """
        try:


            # Create the directory if it does not exist
            os.makedirs(output_dirpath, exist_ok=True)

            if not filename:
                filename = f"language_detection-output-{get_current_time_string()}.txt"

            with open(f"{output_dirpath}/{filename}", "w") as file:
                # file.write(f"Language Detection Results (Timestamp: {self.timestamp}):\n")
                for entry in self.data:
                    file.write(f"{entry.label}: {entry.value}\n")
            print(f"Results saved to {output_dirpath}/{filename}")

        except Exception as exc:
            print(f"Error saving results: {exc}")
