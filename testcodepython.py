import unittest
from codepython import calculate_bill_logic, reset_fields_logic

class TestBillCalculator(unittest.TestCase):
    def test_calculate_bill_water(self):
        result = calculate_bill_logic(200, 100, 50, "Single Bed", "Water Bill")
        self.assertEqual(result["total_bill"], 1750)
        self.assertEqual(result["progress"], 100)

    def test_calculate_bill_error(self):
        result = calculate_bill_logic(100, 200, 50, "Single Bed", "Water Bill")
        self.assertEqual(result["status"], "warning")

    def test_reset_fields(self):
        fields = reset_fields_logic()
        self.assertEqual(fields["last_meter"], "")
        self.assertEqual(fields["progress"], 0)

if __name__ == "__main__":
    unittest.main()
