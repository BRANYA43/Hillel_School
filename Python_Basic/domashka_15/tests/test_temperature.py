import unittest
from tasks import temperature


class TemperatureTest(unittest.TestCase):
    def setUp(self):
        self.number = 25
        self.response_number = {'kelvin': [25.0, 298.14, 269.26],
                                'celsius': [-248.15, 25.0, -3.89],
                                'fahrenheit': [-414.67, 77.0, 25.0]}
        self.scale = ['K', 'C', 'F']

    def test_kelvin(self):
        for scale, response in zip(self.scale, self.response_number['kelvin']):
            self.assertEqual(response, temperature.get_kelvin(self.number, scale))

    def test_get_celsius(self):
        for scale, response in zip(self.scale, self.response_number['celsius']):
            self.assertEqual(response, temperature.get_celsius(self.number, scale))

    def test_get_fahrenheit(self):
        for scale, response in zip(self.scale, self.response_number['fahrenheit']):
            self.assertEqual(response, temperature.get_fahrenheit(self.number, scale))

    def test_is_int(self):
        pass

    def test_is_float(self):
        pass

    def test_get_input_number_element_list(self):
        pass

    def test_et_input_number_int_or_float(self):
        pass

    def test_get_round_off_number(self):
        pass
