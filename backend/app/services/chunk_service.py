from sqlalchemy.orm import Session

from app.model.document_chunk import DocumentChunk
from app.services.embedding_service import create_embedding


def split_text(
        text: str,
        chunk_size: int = 500,
        overlap: int = 100,
):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks

def save_chunks(
        db: Session,
        document_id: int,
        page_number: int,
        chunks: list[str],
):
    for index,content in enumerate(chunks):
        embedding = create_embedding(content)
        chunk = DocumentChunk(
            document_id=document_id,
            page_number=page_number,
            chunk_index = index,
            content=content,
            embedding=embedding
        )

        db.add(chunk)
