import unittest
import importlib
asgmt = importlib.import_module("asgmt-zero")

class TestAssignmentZero(unittest.TestCase):
    def test_01_subtract(self):
        self.assertEqual(asgmt.subtract(5, 6), -1)
        self.assertEqual(asgmt.subtract(55, 66), -11)
        self.assertEqual(asgmt.subtract(8, 7), 1)
    def test_02_convert_celsius_to_fahrenheit(self):
        self.assertTrue(asgmt.convert_celsius_to_fahrenheit(0) >= 32.0)
        self.assertTrue(asgmt.convert_celsius_to_fahrenheit(100) >= 212.0)
    def test_03_sort_a_list(self):
        unsorted_list = [3, 2, 5]
        self.assertEqual(asgmt.sort_a_list(unsorted_list), [2, 3, 5])
        unsorted_list = [13, 7, 11]
        self.assertEqual(asgmt.sort_a_list(unsorted_list), [7, 11, 13])

suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentZero)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))