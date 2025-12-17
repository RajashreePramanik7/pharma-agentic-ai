from flask import Flask, request, jsonify

app = Flask(__name__)

WEB_RESULTS = [
    {
        "title": "GINA 2024 Asthma Guidelines",
        "url": "https://example.org/gina-asthma",
        "snippet": "Updated asthma management recommendations for adults and children."
    },
    {
        "title": "WHO Burden of COPD in India",
        "url": "https://example.org/who-copd-india",
        "snippet": "Summary of COPD prevalence and mortality trends in India."
    },
]

@app.route("/web-search", methods=["GET"])
def web_search():
    q = request.args.get("q", "").lower()
    # For mock, always return all; you can filter by q if needed
    return jsonify({"results": WEB_RESULTS})

if __name__ == "__main__":
    app.run(port=7005, debug=True)
