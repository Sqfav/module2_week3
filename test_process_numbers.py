from process_numbers import process_numbers
import unittest


class TestProcessNumbers(unittest.TestCase):
    def test_process_numbers_standard(self):
        self.assertEqual(process_numbers([1, 2, 3, 4, 5, -2, -4]), 20)

    def test_empty_list(self):
        self.assertEqual(process_numbers([]), 0)

    def test_no_even(self):
        self.assertEqual(process_numbers([1, 3, 5, 7]), 0)

    def test_one_number(self):
        self.assertEqual(process_numbers([2]), 4)

if __name__ == '__main__':
    unittest.main()