import unittest
from oxrse_unit_conv.units import celsius, kelvin


class TestCelsius(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(celsius.si_unit.matches(kelvin))

    def test_basic_conversion(self):
        self.assertEqual(celsius.to_si(0), 273.15)
        self.assertAlmostEqual(celsius.to_unit(10, celsius), 10, 8)


if __name__ == '__main__':
    unittest.main()
