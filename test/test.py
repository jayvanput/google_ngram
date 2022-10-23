import json
import google_ngram
import unittest

class TestGoogleNgram(unittest.TestCase):

    def test_request_returns_dict(self):
        ngram = google_ngram.GoogleNgram()
        ngram.set_param("content", "Albert+Einstein")
        
        ngram.request_data()

        self.assertIsInstance(ngram.data, dict)

    def test_bad_url_raises_error(self):
        ngram = google_ngram.GoogleNgram()
        self.assertRaises(Exception, ngram.request_data)

    def test_content_isnt_give(self):
        ngram = google_ngram.GoogleNgram()
        ngram.set_param("start_year", "2000")
        
        self.assertRaises(Exception, ngram.request_data)

    def test_multiple_contents_returns_each(self):
        ngram = google_ngram.GoogleNgram()
        ngram.set_param("content", "Albert+Einstein")
        ngram.set_param("content", "Frankenstein")
        
        ngram.request_data()

        self.assertEqual(len(ngram.data), 2)

    
if __name__ == "__main__":
    unittest.main()