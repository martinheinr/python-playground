#!/usr/bin/env python3

import unittest

from raising_errors import validate_user

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)
  
  def test_invalid_minlen(self):
    #Parameters are Error, function_name, parameter 1 and parameter 2
    #This test does try - catch in the background and tries to catch
    #the error we told it to catch (ValueError)
    self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()