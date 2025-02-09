import ccxt
from flask import Flask, jsonify, request

app = Flask(__name__)

# 初始化交易所（这里以Binance为例）
coinbase = ccxt.coinbase()
binance = ccxt.binance()

@app.route('/coinbase_price', methods=['GET'])
def get_coinbase_price():
    symbol = request.args.get('symbol', 'BTC/USDT')
    try:
        ticker = coinbase.fetch_ticker(symbol)
        return jsonify({
            'symbol': symbol,
            'price': ticker['last']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/binance_price', methods=['GET'])
def get_binance_price():
    symbol = request.args.get('symbol', 'BTC/USDT')
    try:
        ticker = binance.fetch_ticker(symbol)
        return jsonify({
            'symbol': symbol,
            'price': ticker['last']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/test', methods=['GET'])
def test():
  try:
      markets = coinbase.load_markets()
      print(markets.keys())  # 打印支持的交易对
  except Exception as e:
      print(f"Error loading markets: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
