from sqlalchemy.orm import Session

from app.model.document_chunk import DocumentChunk
from app.services.embedding_service import create_embedding

def search_similar_chunks(
        db: Session,
        query: str,
        top_k: int = 5,
):
    query_embedding = create_embedding(query)

    results = (
        db.query(DocumentChunk,
                 DocumentChunk.embedding.cosine_distance(
                     query_embedding
                 ).label("distance"),
                 )
        .order_by(
            DocumentChunk.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(top_k)
        .all()
    )
    return [
        {
            "id" : chunk.id,
            "document_id": chunk.document_id,
            "page_number": chunk.page_number,
            "chunk_index": chunk.chunk_index,
            "content": chunk.content,
            "distance": distance,
            "similarity": 1-distance,
        }
        for chunk,distance in results
    ]