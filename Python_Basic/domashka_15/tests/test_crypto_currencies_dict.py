import unittest
from tasks import crypto_currencies_dict


class CryptoCurrenciesDictTest(unittest.TestCase):
    def setUp(self):
        self.coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
        self.code = ('BTC', 'ETH', 'XRP', 'LTC')
        self.ret = {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

    def test_create_dict(self):
        self.assertIs(dict, type(crypto_currencies_dict.create_dict(self.coin, self.code)))
        self.assertEqual(self.ret, crypto_currencies_dict.create_dict(self.coin, self.code))
