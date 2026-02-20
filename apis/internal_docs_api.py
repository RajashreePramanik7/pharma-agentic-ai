from flask import Flask, request, jsonify

app = Flask(__name__)

INTERNAL_DOCS = [
    {
        "id": "DOC001",
        "title": "Respiratory Strategy FY25",
        "tags": ["respiratory", "india", "strategy"],
        "summary": "High patient burden, moderate competition, focus on ICS/LABA combos."
    },
    {
        "id": "DOC002",
        "title": "Diabetes GLP1 Field Insights",
        "tags": ["diabetes", "glp1", "field"],
        "summary": "Strong uptake in urban centers, price sensitivity in rural regions."
    },
]

@app.route("/internal-search", methods=["GET"])
def internal_search():
    query = request.args.get("q", "").lower()
    matches = []
    for d in INTERNAL_DOCS:
        text = " ".join([d["title"]] + d["tags"] + [d["summary"]]).lower()
        if query in text:
            matches.append(d)
    return jsonify({"documents": matches})

if __name__ == "__main__":
    app.run(port=7004, debug=True)
