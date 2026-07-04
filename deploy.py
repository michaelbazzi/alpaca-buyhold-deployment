from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from config import API_KEY, API_SECRET

client = TradingClient(API_KEY, API_SECRET, paper=True)

tickers = ["AAPL", "MSFT", "JPM", "XOM", "JNJ"]

account = client.get_account()
buying_power = float(account.cash)
allocation_per_stock = buying_power * 0.20

positions = client.get_all_positions()
held_tickers = [p.symbol for p in positions]

for ticker in tickers:
    if ticker in held_tickers:
        print(f"Already holding {ticker}, skipping.")
        continue
    order = MarketOrderRequest(
        symbol=ticker,
        notional=round(allocation_per_stock, 2),
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
    )
    client.submit_order(order_data=order)
    print(f"Order submitted: {ticker}")

print("Done.")
