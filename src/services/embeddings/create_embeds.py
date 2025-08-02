from google import genai 
from src import GEMINI_API_KEY

async def get_gemini_embeddings(chunks, embedding_model_name="gemini-embedding-001", type="chunks", unique_file_id=None):
    client = genai.Client(api_key=GEMINI_API_KEY)
    result = client.models.embed_content(model=embedding_model_name, contents=chunks)
    if type == "chunks":
        final_embed_result = []
        for i,embedding_data in enumerate(result.embeddings):
            # Add a uuid - unique to each file
            final_embed_result.append({"id": i, "vector": embedding_data.values, "text": chunks[i], "file_id": unique_file_id})
        return final_embed_result
    elif type == "query":
        return result.embeddings[0].values