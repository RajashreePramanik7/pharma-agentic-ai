from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUCT_TRADE = {
    "salbutamol": {"export_kg": 15000, "dependency": "Medium", "countries": ["India", "USA", "UK"]},
    "keytruda": {"export_kg": 2500, "dependency": "Low", "countries": ["USA", "EU", "Japan"]},
    "ozempic": {"export_kg": 8000, "dependency": "High", "countries": ["USA", "Denmark", "China"]},
    "entresto": {"export_kg": 12000, "dependency": "Medium", "countries": ["Switzerland", "USA", "Germany"]},
    "humira": {"export_kg": 3500, "dependency": "Low", "countries": ["USA", "EU", "Canada"]}
}

@app.route('/trade-volume', methods=['GET'])
def trade_volume():
    product = request.args.get('product', 'salbutamol').lower()
    data = PRODUCT_TRADE.get(product, PRODUCT_TRADE['salbutamol'])
    return jsonify({
        "api_name": product.title(),
        "export_volume_kg": data["export_kg"],
        "import_dependency": data["dependency"],
        "countries": data["countries"]
    })

if __name__ == "__main__":
    app.run(port=7001, debug=True)
