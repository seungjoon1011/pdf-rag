from app.services.pdf_service import extract_text

pages = extract_text(
    "../data/pdfs/sqld.pdf"
)

for index, text in enumerate(pages):
    print("=" * 50)
    print(f"PAGE {index + 1}")
    print("=" * 50)
    print(text)