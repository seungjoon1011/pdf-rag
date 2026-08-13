from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.document import DocumentCreate
from app.services.document_service import (
    create_document as create_document_service,
    get_documents as get_documents_service,
    get_document as
    get_document_service,                                    )

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("")
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)):
    return create_document_service(db, document)


@router.get("")
def get_documents(
    db: Session = Depends(get_db)
):
    return get_documents_service(db)

@router.get("/{document_id}")
def get_document(document_id: int,
                 db: Session = Depends(get_db)):
    return get_document_service(db, document_id)