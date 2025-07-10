from flask import Flask, request, jsonify
from api_cupones import get_final_price

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def get_price():
    data = request.get_json()
    price = data.get("price")
    coupon = data.get("coupon")
    tax_rate = data.get("impuesto", 0.19)

    final = get_final_price(price, coupon, tax_rate)
    return jsonify({"precio_final": final})