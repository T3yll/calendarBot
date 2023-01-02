from pybit import inverse_perpetual

session = inverse_perpetual.HTTP(
    endpoint='https://api.bybit.com', 
    api_key='...',
    api_secret='...'
)
ws = inverse_perpetual.WebSocket(
    test=False,
    api_key="...",
    api_secret="..."
)

# Get orderbook.
session.orderbook(symbol='BTCUSD')

# Create five long orders.
orders = [{
    "symbol": "BTCUSD", 
    "order_type": "Limit", 
    "side": "Buy", 
    "qty": 100, 
    "price": i,
    "time_in_force": "GoodTillCancel"
} for i in [5000, 5500, 6000, 6500, 7000]]

# Submit the orders in bulk.
session.place_active_order_bulk(orders)

# Check on your order and position through WebSocket.
def handle_orderbook(message):
    print(message)
def handle_position(message):
    print(message)

ws.orderbook_25_stream(handle_orderbook, "BTCUSD")
ws.position_stream(handle_position)

while True:
    # Run your main trading strategy here
    pass  # To avoid CPU utilisation, use time.sleep(1)