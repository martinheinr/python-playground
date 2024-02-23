""" The building blocks of unit tests within the unittest module are test cases, which enable developers to run multiple tests at once. 
To write test cases, developers need to write subclasses of TestCase or use FunctionTestCase. 

To perform a specific test, the TestCase subclass needs to implement a test method that starts with the name test. 
This identifier is what informs the test runner about which methods represent tests.
 """

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase), expected)
    
  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
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
