from fastapi import FastAPI

from app.api.documents import router as document_router
from app.core.database import Base,engine

from app.model.document import Document

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(document_router)

@app.get("/")
def root():
	return {"message": "Hello PDF RAG"}

@app.get("/health")
def health():
	return {"status": "ok"}
