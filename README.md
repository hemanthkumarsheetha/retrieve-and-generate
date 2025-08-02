# Retrieve and Generate

A RAG (Retrieval-Augmented Generation) application with FastAPI and Streamlit for document processing and question answering.

## Installation

Install dependencies using uv:

```bash
uv sync
```

## Running the API

Start the FastAPI server:

```bash
uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Create Embeddings

Upload a PDF file to create embeddings:

```bash
curl -X POST "http://localhost:8000/api/v1/create_embeddings/for-a-single-file" \
  -H "X-API-Key: your-api-key" \
  -F "file=@your-document.pdf"
```

Response:
```json
{
  "status": "done",
  "file_id": "uuid-string"
}
```

### Query

Ask questions about uploaded documents:

```bash
curl -X POST "http://localhost:8000/api/v1/query/get-answers" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "question": "What is the main topic of the document?",
    "file_id": "uuid-string"
  }'
```

Response:
```json
{
  "answer": "The main topic is..."
}
```

## Running Streamlit

Launch the Streamlit web interface:

```bash
uv run streamlit run streamlit/app.py
```

The Streamlit app will be available at `http://localhost:8501`