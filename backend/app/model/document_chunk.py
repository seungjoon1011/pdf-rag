from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from app.core.database import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id")
    )

    page_number: Mapped[int]

    chunk_index: Mapped[int]

    content: Mapped[str] = mapped_column(
        Text
    )

    embedding: Mapped[list[float]] = mapped_column(
        Vector(1024)
    )