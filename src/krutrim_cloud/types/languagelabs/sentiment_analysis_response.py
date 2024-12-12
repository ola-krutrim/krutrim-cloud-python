import os
from typing import List, Dict
from ..._models import BaseModel
from ...lib.utils import get_current_time_string

__all__ = ["SentimentAnalysisResponse"]

class SentimentAnalysisResponse(BaseModel):
    status: str
    data: List[Dict[str, List[str]]]
    http_status: str
    timestamp: int
    code: int

    def save(self, output_dirpath: str, filename: str = ""):
        """
        Saves the sentiment analysis results to a text file .
        """
        try:

            # Create the directory if it does not exist
            os.makedirs(output_dirpath, exist_ok=True)

            if not filename:
                filename = f"sentiment_analysis_result-{get_current_time_string()}.txt"

            with open(f"{output_dirpath}/{filename}", "w") as file:
                # file.write(f"Sentiment Analysis Result (Timestamp: {self.timestamp}):\n")
                for sentiment in self.Sentiment:
                    label = sentiment.get("label")
                    value = sentiment.get("value")
                    file.write(f"Text: {label}\n")
                    file.write(f"Sentiment(s): {', '.join(value)}\n\n")

            print(f"Results saved to {output_dirpath}/{filename}")
        except Exception as exc:
            print(f"Error saving results: {exc}")
