"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:
  Input:
    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
  Output:
    {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}"""

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

cryptocurrencies = {key: item for key, item in zip(coin, code)}
print(cryptocurrencies)
