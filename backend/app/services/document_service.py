from app.schemas.document import DocumentCreate
from sqlalchemy.orm import Session
from app.model.document import Document
from sqlalchemy import select

def create_document(
    db: Session,
    document: DocumentCreate,
    ):
    new_document = Document(
        title=document.title,
        filename=document.filename,
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document

def get_documents(
        db: Session
):
    statement = select(Document)

    result = db.execute(statement)

    return result.scalars().all()

def get_document(
        db: Session,
        document_id: int,
):
    return db.get(Document, document_id)