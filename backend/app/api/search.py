from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.search_service import search_similar_chunks

router = APIRouter(
    prefix="/search",
    tags=["search"],
)

@router.get("")
def search(
    query:str,
    db: Session = Depends(get_db),
):
    return search_similar_chunks(
        db,
        query,
    )