from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.rag_service import answer_question

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@router.get("")
def chat(
    question: str,
    top_k: int = 5,
    db: Session = Depends(get_db),
):
    return answer_question(
        db=db,
        question=question,
        top_k=top_k,
    )