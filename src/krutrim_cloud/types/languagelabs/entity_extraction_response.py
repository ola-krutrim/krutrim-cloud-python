import os
from typing import List, Dict
from ..._models import BaseModel
from ...lib.utils import get_current_time_string

__all__ = ["EntityExtractionResponse", "EntityExtractionData", "EntityExtractionItem"]

class EntityExtractionItem(BaseModel):
    label: str
    value: str

class EntityExtractionData(BaseModel):
    title: str
    color: str
    data: List[EntityExtractionItem]

class EntityExtractionResponse(BaseModel):
    status: str
    data: List[EntityExtractionData]
    Total_entities: int
    http_status: str
    timestamp: int
    code: int


    def save(self, output_dirpath: str, filename: str = ""):
        """
        Saves the entity extraction results to a text file.
        """
        try:

            # Create the directory if it does not exist
            os.makedirs(output_dirpath, exist_ok=True)

            if not filename:
                filename = f"entity_extraction_results-{get_current_time_string()}.txt"

            with open(f"{output_dirpath}/{filename}", "w") as file:
                # file.write(f"Entity Extraction Results (Timestamp: {self.timestamp}):\n")
                # file.write(f"Total Entities: {self.Total_entities}\n")
                for entity_data in self.data:
                    file.write(f"\nTitle: {entity_data.title} (Color: {entity_data.color})\n")
                    for item in entity_data.data:
                        file.write(f"  {item.label}: {item.value}\n")

            print(f"Results saved to {output_dirpath}/{filename}")
        except Exception as exc:
            print(f"Error saving results: {exc}")
