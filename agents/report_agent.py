from fpdf import FPDF

def generate_report(query, summary, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 8, f"Query:\n{query}\n\nSummary:\n{summary}")
    path = f"static/reports/{query[:10].replace(' ', '_')}.pdf"
    pdf.output(path)

    return f"/{path}"
