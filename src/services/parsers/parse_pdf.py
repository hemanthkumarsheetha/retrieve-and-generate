from pypdf import PdfReader

async def get_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    pages = reader.pages
    all_text = ""
    for page in pages:
        all_text += page.extract_text()
    return all_text