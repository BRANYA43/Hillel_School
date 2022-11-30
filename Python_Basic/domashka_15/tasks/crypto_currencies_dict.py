"""Дано два кортежі, напишіть функцію яка з'єднає їх в один dict:
  Input:
    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
  Output:
    {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}"""


def create_dict(keys: tuple | list, items: tuple | list) -> dict:
    return {key: item for key, item in zip(keys, items)}


if __name__ == '__main__':
    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
    print(create_dict(coin, code))
