from flask import Flask, request, jsonify

app = Flask(__name__)

TRIALS = [
    {
        "nct_id": "NCT0000001",
        "indication": "asthma",
        "moa": "beta-2 agonist",
        "phase": "Phase 3",
        "status": "Recruiting",
        "sponsor": "PharmaCo A",
        "country": "India"
    },
    {
        "nct_id": "NCT0000002",
        "indication": "asthma",
        "moa": "beta-2 agonist",
        "phase": "Phase 2",
        "status": "Completed",
        "sponsor": "PharmaCo B",
        "country": "USA"
    },
]

@app.route("/clinical-trials", methods=["GET"])
def clinical_trials():
    indication = request.args.get("indication", "").lower()
    country = request.args.get("country", "").lower()
    moa = request.args.get("moa", "").lower()

    results = []
    for t in TRIALS:
        if indication and indication not in t["indication"].lower():
            continue
        if country and country.lower() != t["country"].lower():
            continue
        if moa and moa not in t["moa"].lower():
            continue
        results.append(t)

    return jsonify({"trials": results})

if __name__ == "__main__":
    app.run(port=7003, debug=True)
