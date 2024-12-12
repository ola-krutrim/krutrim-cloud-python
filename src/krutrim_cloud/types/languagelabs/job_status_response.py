from typing import Optional
from ..._models import BaseModel

__all__ = ["JobStatusResponse", "JobStatusData"]

class JobStatusData(BaseModel):
    request_id: str  # Unique identifier for the long-duration request
    file_name: str  # The name of the file being processed
    file_size_mb: float  # The size of the file in megabytes
    service_type: str  # The service used for the processing (e.g., "stttransservice")
    status: str  # The current status of the job (e.g., "SUCCESS", "QUEUED", "IN_PROGRESS")
    output_file: Optional[str] = None  # URL for downloading the output file (if available)
    created_at: str  # Timestamp when the request was created
    updated_at: str  # Timestamp when the status was last updated

class JobStatusResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: JobStatusData  # Contains details about the job status and the result

