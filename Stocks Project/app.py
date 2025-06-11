from flask import Flask, render_template, request, jsonify
import yfinance as yf
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/stock")
def stock_data():
    symbol = request.args.get("symbol", "").upper()
    period = request.args.get("range", "5d")

    if not symbol:
        return jsonify({"error": "No symbol provided"}), 400

    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)

        if hist.empty:
            return jsonify({"error": "No data found for symbol."}), 404

        dates = hist.index.strftime("%Y-%m-%d").tolist()
        prices = hist["Close"].round(2).tolist()

        # Remove NaN values
        clean_dates = []
        clean_prices = []

        for d, p in zip(dates, prices):
            if p is not None and not (isinstance(p, float) and math.isnan(p)):
                clean_dates.append(d)
                clean_prices.append(p)

        latest_price = clean_prices[-1] if clean_prices else "N/A"

        return jsonify({
            "symbol": symbol,
            "dates": clean_dates,
            "prices": clean_prices,
            "latest_price": latest_price
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
