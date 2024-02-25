import unittest

ORIGINAL_FILE_PATH = "C:/test_files/test_results.txt"
COUNTER = 0

def simple_addition(a, b):
    return a + b

class TestSimpleAddition(unittest.TestCase):

    def setUp(self):
        global COUNTER
        COUNTER += 1
    
    def write_result_to_file(self, result):
        with open(ORIGINAL_FILE_PATH, 'a') as file:
            file.write(f"Test {COUNTER}: {result}\n")

    def test_add_positive_numbers_å(self):
        try:
            self.assertTrue(simple_addition(1, 1) == 2)
            result = "PASSED"
        except AssertionError:
            result = "FAILED"
        self.write_result_to_file(result)

    def test_add_positive_numbers(self):
        result = "PASSED" if simple_addition(1, 1) == 2 else "FAILED"
        self.write_result_to_file(result)

    def test_use_simple_number(self):
	    self.assertEqual(simple_addition(1, 1), 2)
    
    
unittest.main()