import os
from fastapi import APIRouter, UploadFile, File
from models.api_models import EmbedAFile, EmbedAFileResult
from src.utils.auth import require_api_key
from src.services.rag.retrieve import create_embeds_for_single_pdf_file

router = APIRouter(prefix="/api/v1/create_embeddings", tags=["create_embeddings"])


async def read_file(file: UploadFile):
    content = await file.read()
    os.makedirs("/tmp/",exist_ok=True)
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(content)
    return file_path

@router.post("/for-a-single-file")
@require_api_key
async def embed_a_single_file(file: UploadFile = File()):
    file_path = await read_file(file)
    _, file_id = await create_embeds_for_single_pdf_file(file_path)
    status = "done"
    return EmbedAFileResult(status=status, file_id=file_id)