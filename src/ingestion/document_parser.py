def parse_pdf(file_path):
    import PyPDF2
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_docx(file_path):
    from docx import Document
    text = ""
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def parse_xlsx(file_path):
    import pandas as pd
    df = pd.read_excel(file_path)
    return df.to_string()

def parse_document(file_path):
    import os
    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".pdf":
        return parse_pdf(file_path)
    elif file_extension == ".docx":
        return parse_docx(file_path)
    elif file_extension == ".xlsx":
        return parse_xlsx(file_path)
    else:
        raise ValueError("Unsupported file format: {}".format(file_extension))