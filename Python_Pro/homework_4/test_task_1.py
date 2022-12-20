import unittest

from Python_Pro.homework_4.task_1 import DigitalCounter


class TestDigitalCounter(unittest.TestCase):
    def setUp(self):
        self.digital_counters = [DigitalCounter(),
                                 DigitalCounter(10, 110),
                                 DigitalCounter(10, 200, 100)]

    def test_get_current_value(self):
        checker_values = [0, 10, 100]
        for counter, value in zip(self.digital_counters, checker_values):
            self.assertEqual(value, counter.get_current_value())

    def test_increase(self):
        checker_values = [1, 11, 101]
        for counter, value in zip(self.digital_counters, checker_values):
            counter.increase()
            self.assertEqual(value, counter.get_current_value())

        checker_values = [100, 110, 200]
        for counter, value in zip(self.digital_counters, checker_values):
            for _ in range(100):
                counter.increase()
            self.assertEqual(value, counter.get_current_value())


if __name__ == '__main__':
    unittest.main()
