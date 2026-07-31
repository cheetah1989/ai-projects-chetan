import docx
from pypdf import PdfReader
from pathlib import Path


def _read_txt(path: Path) -> str:
    """ Internal function to read text files"""
    return path.read_text(encoding="utf-8")


def _read_docx(path: Path) -> str:
    """ Internal function to read docx files"""
    doc = docx.Document(path)
    return "\n".join(para.text for para in doc.paragraphs)


def _read_pdf(path: Path) -> str:
    """ Internal function to read PDF files as transcript"""
    reader = PdfReader(path)
    text_pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_pages.append(text)

    return "\n".join(text_pages)


def read_transcript(file_path: str) -> str:
    """ Public API to read the txt, docx and pdf format of a transcript"""
    path = Path(file_path)

    if not path.is_file():
        raise ValueError(f"The transcript is not found in path: {file_path}")

    extension = path.suffix.lower()
    readers = {
        ".txt": _read_txt,
        ".docx": _read_docx,
        ".pdf": _read_pdf
    }

    # Call internal functions based on the extension of the file
    reader = readers.get(extension)
    if reader is None:
        raise ValueError(
            "Unsupported extension for the input transcript file: \n Only .txt .docx or .pdf are support currently! ")

    return reader(path)
