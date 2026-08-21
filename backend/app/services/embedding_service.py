from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session

from app.model.document_chunk import DocumentChunk

model = SentenceTransformer(
    "BAAI/bge-m3"
)

def create_embedding(text: str):
    return model.encode(text).tolist()

def embed_chunks(db: Session):
    chunks = db.query(DocumentChunk).all()

    for chunk in chunks:
        chunk.embedding = create_embedding(
            chunk.content
        )

    db.commit()