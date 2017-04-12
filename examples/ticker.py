import poloniex
polo = poloniex.Poloniex()
polo.timeout = 2
print(polo.marketTradeHist('BTC_ETH', 1491968580, 1491968590))

