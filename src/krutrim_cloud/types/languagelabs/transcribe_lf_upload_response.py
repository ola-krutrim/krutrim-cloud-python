from ..._models import BaseModel

__all__ = ["TranscribeLfUploadResponse", "TranscribeLfUploadData"]

class TranscribeLfUploadData(BaseModel):
    request_id: str  # Unique identifier for the transcription request
    status: str  # The status of the transcription request (e.g., "QUEUED", "IN_PROGRESS", "COMPLETED")

class TranscribeLfUploadResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: TranscribeLfUploadData  # Contains request_id and status of the transcription
