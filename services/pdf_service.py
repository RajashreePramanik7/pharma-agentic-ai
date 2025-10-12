from reportlab.pdfgen import canvas

def generate_pdf(content, filename="report.pdf"):
    path = f"static/reports/{filename}"
    pdf = canvas.Canvas(path)
    pdf.drawString(50, 800, "Agentic AI - Pharma Report")
    pdf.drawString(50, 780, content)
    pdf.save()
    return path
