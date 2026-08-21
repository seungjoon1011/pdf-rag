from app.core.database import SessionLocal
from app.model.document import Document
from app.model.document_chunk import DocumentChunk

from app.services.embedding_service import embed_chunks

db = SessionLocal()

embed_chunks(db)

db.close()