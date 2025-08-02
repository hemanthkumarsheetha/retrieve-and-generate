from src.services.embeddings.vector_db import VectorDB
from src.services.embeddings.create_embeds import get_gemini_embeddings
from src.services.parsers.parse_pdf import get_text_from_pdf
from src.services.chunkers.chunk_text import Chunkers
import uuid

vector_db = VectorDB()

async def retrieve_chunks(query, file_id):
    # ids, file_id = await create_embeds_for_single_pdf_file(file_path)
    query_embedding = await get_gemini_embeddings([query], type="query", unique_file_id=file_id)
    retrieve_chunks = vector_db.search_data(query_embedding, file_id)
    return retrieve_chunks

async def create_embeds_for_single_pdf_file(file_path):
    all_file_text = await get_text_from_pdf(file_path)
    chunker = Chunkers(all_file_text)
    chunks = chunker.chunk_text_based_on_structure()
    if chunks:
        chunks = [chunk.page_content for chunk in chunks]
    unique_file_id = str(uuid.uuid4())
    embedding_data = await get_gemini_embeddings(chunks, unique_file_id=unique_file_id)
    ids = vector_db.insert_data(embedding_data)
    return ids, unique_file_id