"""
Test suite for earquake ADT
"""
import unittest
from Earthquake import Earthquake

class EarthquakeTest(unittest.TestCase):
    def setUp(self):
        self.earthquake = Earthquake()
    
    def test_earthquake_obj_exist(self):
        self.assertIsNotNone(self.earthquake)
        self.assertIsInstance(self.earthquake, Earthquake)
    
    def test_earthquake_mag_list_check(self):
        month = 1
        mag_list = self.earthquake.getMagnitudeFromMonth(month)

        self.assertIsInstance(mag_list, list)
        self.assertGreater(len(mag_list), 0, 
                           f"No magnitude data found for month {month}")
        
    def test_magnitude_values_are_numeric(self):
        month = 1
        mag_list = self.earthquake.getMagnitudeFromMonth(month)
        
        for mag in mag_list:
            self.assertIsInstance(mag, (int, float), 
                                 f"Magnitude value {mag} is not numeric")
    
    def test_invalid_month(self):
        mag_list = self.earthquake.getMagnitudeFromMonth(13)  # Invalid month
        self.assertEqual(len(mag_list), 0, 
                        "Should return empty list for invalid month")

if __name__ == '__main__':
    unittest.main()