from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.documents import router as document_router
from app.core.database import Base,engine
from app.model.document import Document
from app.model.document_chunk import DocumentChunk
# from app.model.document_page import DocumentPage
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"http://localhost:5173",
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.include_router(document_router)

@app.get("/")
def root():
	return {"message": "Hello PDF RAG"}

@app.get("/health")
def health():
	return {"status": "ok"}
