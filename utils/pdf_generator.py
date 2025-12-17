from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid

PDF_DIR = Path("generated_pdfs")
PDF_DIR.mkdir(exist_ok=True)

def generate_portfolio_pdf(data: dict) -> Path:
    filename = f"portfolio_{uuid.uuid4().hex}.pdf"
    pdf_path = PDF_DIR / filename

    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica", 11)

    c.drawString(50, y, "Agentic AI Pharma Portfolio Report")
    y -= 30

    for key, value in data.items():
        if key == "summary_table":
            continue
        c.drawString(50, y, f"{key}: {str(value)[:100]}")
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return pdf_path