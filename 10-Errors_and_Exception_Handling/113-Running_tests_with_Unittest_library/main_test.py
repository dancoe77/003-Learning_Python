import unittest
import main

class TestMain(unittest.TestCase):

    def test_one_word(self):
        text = "golang"
        result = main.cap_text(text)
        self.assertEqual(result,"Golang")
    def test_multiple_words(self):
        text = "golang rocks"
        result = main.cap_text(text)
        self.assertEqual(result,"Golang Rocks")
if __name__ == "__main__":
    unittest.main()