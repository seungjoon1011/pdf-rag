from pathlib import Path

from pypdf import PdfReader


def extract_text(file_path: str):
    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        pages.append(text or "")

    return pages