import unittest
from codepython import calculate_bill_logic, reset_fields_logic

class TestBillCalculator(unittest.TestCase):
    def test_water_bill(self):
        result = calculate_bill_logic(150, 100, 10, "Single Bed", "Water Bill")
        self.assertEqual(result["total_bill"], 10 * 5 + 1500)
        self.assertEqual(result["progress"], 100)

    def test_electric_bill(self):
        result = calculate_bill_logic(200, 150, 20, "Double Bed", "Electric Bill")
        self.assertEqual(result["total_bill"], 20 * 6 + 2000)
        self.assertEqual(result["progress"], 100)

    def test_invalid_meter(self):
        result = calculate_bill_logic(100, 150, 10, "Single Bed", "Water Bill")
        self.assertEqual(result["status"], "warning")

    def test_progress_50(self):
        result = calculate_bill_logic(150, 100, 10, "", "Water Bill")
        self.assertEqual(result["progress"], 50)

    def test_reset(self):
        fields = reset_fields_logic()
        self.assertEqual(fields["progress"], 0)
        self.assertEqual(fields["room_type"], "Please Select")

if __name__ == "__main__":
    unittest.main()
