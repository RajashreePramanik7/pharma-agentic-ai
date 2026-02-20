from flask import Flask, request, jsonify
from flask import make_response
import io
from reportlab.pdfgen import canvas  # pip install reportlab

app = Flask(__name__)

@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.json or {}
    title = data.get("title", "Portfolio Analysis Report")
    sections = data.get("sections", [])

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, title)
    y -= 40
    p.setFont("Helvetica", 10)
    for sec in sections:
        if y < 80:
            p.showPage()
            y = 800
            p.setFont("Helvetica", 10)
        p.drawString(50, y, f"{sec.get('heading', '')}: {sec.get('text', '')[:200]}")
        y -= 20
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=report.pdf"
    return response

if __name__ == "__main__":
    app.run(port=7006, debug=True)
