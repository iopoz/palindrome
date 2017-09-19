import unittest

import main_script


class PalindromeTests(unittest.TestCase):
    def setUp(self):
        self._palindrome = main_script

    def test_correct_data(self):
        self.assertTrue(self._palindrome.is_palindrome("А роза упала на лапу Азора"))

    def test_incorrect_data(self):
        self.assertFalse(self._palindrome.is_palindrome("Hello"))


if __name__ == "__main__":
    unittest.main()
