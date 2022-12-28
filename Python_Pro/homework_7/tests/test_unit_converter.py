import unittest

from Python_Pro.homework_7.utils.unit_converter import UnitConverter


class TestUnitConvertor(unittest.TestCase):
    def setUp(self):
        self.unit_converter = UnitConverter()

    def test_get_convert_value(self):
        po = 'po'
        kg = 'kg'
        check_value = 100
        check_results = (45.36, 220.46)
        res = self.unit_converter.convert(po, kg, 100)
        self.assertEqual(check_results[0], res)
        res = self.unit_converter.convert(kg, po, 100)
        self.assertEqual(check_results[1], res)


if __name__ == '__main__':
    unittest.main()
