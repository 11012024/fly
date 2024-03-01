from pybit.unified_trading import HTTP


def main():
    client = HTTP()
    tickers = client.get_tickers(category="spot")
    for ticker in tickers['result']['list']:
        symbol = ticker['symbol']
        response = client.get_orderbook(category="spot", symbol=symbol)
        print(response['result'])


if __name__ == "__main__":
    main()
