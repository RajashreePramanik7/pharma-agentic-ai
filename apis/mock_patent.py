from flask import Flask, request, jsonify

app = Flask(__name__)

PATENT_DATA = {
    "salbutamol": {"number": "US6789012B2", "expiry": "2028-03-15", "fto": "Clear", "filings": 12},
    "keytruda": {"number": "US8383787B2", "expiry": "2034-11-20", "fto": "Warning", "filings": 45},
    "ozempic": {"number": "US7919099B2", "expiry": "2032-09-10", "fto": "Clear", "filings": 28},
    "entresto": {"number": "US8653107B2", "expiry": "2033-05-22", "fto": "Clear", "filings": 19},
    "humira": {"number": "US6090382B2", "expiry": "2029-07-14", "fto": "Litigation", "filings": 67}
}

@app.route('/patent-status', methods=['GET'])
def patent_status():
    product = request.args.get('product', 'salbutamol').lower()
    data = PATENT_DATA.get(product, PATENT_DATA['salbutamol'])
    return jsonify({
        "patent_number": data["number"],
        "expiry_date": data["expiry"],
        "fto_flag": data["fto"],
        "competitor_filings": data["filings"]
    })

if __name__ == "__main__":
    app.run(port=7002, debug=True)
