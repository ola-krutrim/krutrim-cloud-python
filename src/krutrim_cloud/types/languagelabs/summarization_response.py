import os
from typing import Dict
from ..._models import BaseModel
from ...lib.utils import get_current_time_string

__all__ = ["SummarizationResponse"]

class SummarizationResponse(BaseModel):
    status: str
    data: Dict[str, str]
    http_status: str
    timestamp: int
    code: int

    def save(self, output_dirpath: str, filename: str = ""):
        """
        Saves the summarized text to a text file.
        """
        try:

            # Create the directory if it does not exist
            os.makedirs(output_dirpath, exist_ok=True)

            if not filename:
                filename = f"summarization_result-output-{get_current_time_string()}.txt"

            with open(f"{output_dirpath}/{filename}", "w") as file:
                file.write(f"Summary Text: {self.data.get('summaryText')}\n")
            print(f"Results saved to {output_dirpath}/{filename}")
        except Exception as exc:
            print(f"Error saving results: {exc}")
