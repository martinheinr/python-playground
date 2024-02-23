from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test__numbers(self):
    testcase = 1
    expected = "Numbers are not supported"
    self.assertEqual(rearrange_name(testcase), expected)

  def test__negative_numbers(self):
    testcase = -1
    expected = "Numbers are not supported"
    self.assertEqual(rearrange_name(testcase), expected)

  def test__number_zero(self):
    testcase = 0
    expected = "Numbers are not supported"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_edge_case(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()
