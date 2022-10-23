import json
import google_ngram
import unittest

class TestGoogleNgram(unittest.TestCase):

    def test_request_returns_dict(self):
        ngram = google_ngram.GoogleNgram()
        ngram.request_data("https://books.google.com/ngrams/json?content=Albert+Einstein")

        self.assertIsInstance(ngram.data, dict)

    

if __name__ == "__main__":
    unittest.main()