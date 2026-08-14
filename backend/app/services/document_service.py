from app.schemas.document import DocumentCreate
from sqlalchemy.orm import Session
from app.model.document import Document
from sqlalchemy import select
from fastapi import UploadFile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

UPLOAD_DIR = Path(BASE_DIR / "data/pdfs")

def upload_document(
        db: Session,
        file: UploadFile,
):
    UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer: #write binary (wb)
        buffer.write(file.file.read())

    document = Document(
        title=file.filename,
        filename=file.filename,
        filepath=str(file_path),
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document

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