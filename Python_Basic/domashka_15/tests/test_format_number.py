import unittest
from tasks import format_number


class FormatNumberTest(unittest.TestCase):
    def setUp(self):
        self.format_tel = format_number.FormatTelNum()
        self.tel_nums = ['063-999-99-99', '063 999-99-99', '063-99999-99', '+3806399-999-99', '380639999999']

    def test_is_tel_num(self):
        for num in self.tel_nums:
            self.assertTrue(self.format_tel.is_tel_num(num))
        self.assertFalse(self.format_tel.is_tel_num('063-999-99'))
        self.assertFalse(self.format_tel.is_tel_num('063-999-99-99-99'))

    def test_format_tel_num(self):
        for num in self.tel_nums:
            self.assertIs(str, type(self.format_tel.format_tel_num(num)))
            self.assertEqual('(+38) 063 999-99-99', self.format_tel.format_tel_num(num))
        self.assertEqual('None', self.format_tel.format_tel_num('063-999-99'))
