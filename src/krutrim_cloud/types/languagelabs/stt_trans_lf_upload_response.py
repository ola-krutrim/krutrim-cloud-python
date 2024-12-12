from ..._models import BaseModel

__all__ = ["SttTransLfUploadResponse", "SttTransLfUploadData"]

class SttTransLfUploadData(BaseModel):
    request_id: str  # Unique identifier for the transcription and translation request
    status: str  # The status of the request (e.g., "QUEUED", "IN_PROGRESS", "COMPLETED")

class SttTransLfUploadResponse(BaseModel):
    status: str  # Indicates whether the request was successful(e.g., "success")
    data: SttTransLfUploadData  # Contains request_id and status of the request

