from docx import Document


def load_job_description():

    doc = Document("data/job_description.docx")

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)