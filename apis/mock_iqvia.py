from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/market-size', methods=['GET'])
def market_size():
    return jsonify({
        "therapy_area": "Respiratory",
        "market_size": 2500000,
        "cagr": 7.4,
        "competitors": ["BrandX", "BrandY"]
    })

if __name__ == "__main__":
    app.run(port=7000, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# ALL THERAPY AREAS DATA
THERAPY_DATA = {
    "respiratory": {"size": 50000000, "cagr": 6.8, "competitors": ["GSK", "AstraZeneca", "Teva"]},
    "oncology": {"size": 200000000, "cagr": 12.5, "competitors": ["Merck", "Roche", "Bristol-Myers"]},
    "diabetes": {"size": 85000000, "cagr": 18.2, "competitors": ["Novo Nordisk", "Eli Lilly", "Sanofi"]},
    "cardiac": {"size": 120000000, "cagr": 5.9, "competitors": ["Pfizer", "BMS", "Novartis"]},
    "immunology": {"size": 150000000, "cagr": 14.7, "competitors": ["AbbVie", "J&J", "Amgen"]}
}

@app.route('/market-size', methods=['GET'])
def market_size():
    therapy = request.args.get('therapy', 'respiratory').lower()
    data = THERAPY_DATA.get(therapy, THERAPY_DATA['respiratory'])
    return jsonify({
        "therapy_area": therapy.title(),
        "market_size": data["size"],
        "cagr": data["cagr"],
        "competitors": data["competitors"]
    })

if __name__ == "__main__":
    app.run(port=7000, debug=True)
