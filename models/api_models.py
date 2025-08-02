from pydantic import BaseModel
from fastapi import UploadFile

class HealthCheckResult(BaseModel):
    status: str

class GetAnswersInput(BaseModel):
    question: str
    file_id: str

class GetAnswersResult(BaseModel):
    answer: str

class EmbedAFile(BaseModel):
    file: UploadFile

class EmbedAFileResult(BaseModel):
    status: str
    file_id: str