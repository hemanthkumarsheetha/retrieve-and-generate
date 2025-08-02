from fastapi import APIRouter
from models.api_models import GetAnswersInput, GetAnswersResult
from src.utils.auth import require_api_key
from src.services.rag.generate import generate_a_answer

router = APIRouter(prefix="/api/v1/query", tags=["query"])


@router.post("/get-answers")
@require_api_key
async def get_answers(input: GetAnswersInput):
    answer = await generate_a_answer(input.question, input.file_id)
    return GetAnswersResult(answer=answer)
