from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routers import health_check, create_embeddings, query



app = FastAPI(
    title="Retrieve and Generate API",
    version="1.0.0",
    description="API for RAG functionality"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)

# Include routers
app.include_router(health_check.router)
app.include_router(create_embeddings.router)
app.include_router(query.router)