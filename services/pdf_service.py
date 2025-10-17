from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_pdf(molecule, insights):
    os.makedirs("static/reports", exist_ok=True)
    filename = f"{molecule}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    path = f"static/reports/{filename}"

    pdf = canvas.Canvas(path)
    pdf.setTitle(f"Agentic AI Report - {molecule}")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 800, f"Report for {molecule}")
    pdf.setFont("Helvetica", 12)
    y = 760
    for key, value in insights.items():
        pdf.drawString(50, y, f"{key.capitalize()}: {value}")
        y -= 20
    pdf.save()
    return f"http://127.0.0.1:8000/{path}"
