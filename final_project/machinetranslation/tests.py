import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None),"Can't have null input")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None),"Can't have null input")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()