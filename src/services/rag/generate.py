from google import genai 
from src import GEMINI_API_KEY    
from src.services.rag.retrieve import retrieve_chunks

async def generate_a_answer(query, file_id=None):
    retrieved_chunks = await retrieve_chunks(query, file_id)
    # Need to add re-ranker
    combined_text = await combine_retrieved_chunks(retrieved_chunks)
    answer = await get_answer(query, combined_text)
    try:
        if isinstance(answer, str):
            return answer
        final_answer = answer.candidates[0].content.parts[0].text
    except Exception as e:
        raise e
    return final_answer

async def combine_retrieved_chunks(retrieved_chunks):
    combined_text = "All the chunks listed in order of highest similarity with query"
    for i, chunk in enumerate(retrieved_chunks):
        combined_text += f"\n=====CHUNK {i}======\n"
        combined_text += chunk.get("text")
        combined_text += "\n======================\n"
    return combined_text
    

async def get_answer(query, retrieved_text):
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = f"""
    Given a query, answer it based on the retrieved text

    Query: 
    {query}

    Retrieved Text:
    {retrieved_text}

    Answer should be concise, precise and exactly answer the question. Structure it properly.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )

    # Extract the text from the response
    if response.candidates and len(response.candidates) > 0:
        candidate = response.candidates[0]
        if candidate.content and candidate.content.parts:
            return candidate.content.parts[0].text
        else:
            return "No content generated"
    else:
        return "No response generated"