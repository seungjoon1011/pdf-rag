from sqlalchemy.orm import Session

from app.services.search_service import search_similar_chunks
from app.services.llm_service import generate_answer

def answer_question(
        db: Session,
        question: str,
        top_k: int = 5,
):
    chunks = search_similar_chunks(
        db=db,
        query=question,
        top_k=top_k,
    )
    context = "\n\n".join(
        chunk["content"]
        for chunk in chunks
    )
    answer = generate_answer(
        question=question,
        context=context,
    )
    return {
        "question": question,
        "answer": answer,
        "sources": chunks,
    }