import unittest
from translator import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(englishToFrench(""), None)
        self.assertEqual(frenchToEnglish(""), None)
        self.assertEqual(englishToFrench("Hello"), 'Bonjour')
        self.assertEqual(frenchToEnglish("Bonjour"), 'Hello')
        # englishToFrench("Hello")
        # frenchToEnglish("Bonjour")



if __name__ == '__main__':
    unittest.main()