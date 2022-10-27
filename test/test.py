import json
from typing import List
import google_ngram
import unittest

class TestGoogleNgram(unittest.TestCase):

    def test_request_returns_a_list(self):
        output = google_ngram.request()

        self.assertIsInstance(output, List)

    def test_default_request_returns_albert(self):
        output = google_ngram.request()

        self.assertEqual(output[0]["ngram"], "Albert Einstein")
        
    def test_request_returns_input(self):
        output = google_ngram.request("Frankenstein")

        self.assertEqual(output[0]["ngram"], "Frankenstein")

    def test_request_with_multiple_request_values(self):
        output = google_ngram.request(["Albert Einstein", "Frankenstein"])

        self.assertEqual(output[0]["ngram"], "Albert Einstein")
        self.assertEqual(output[1]["ngram"], "Frankenstein")

    def test_can_add_content_for_request(self):
        pass
#     def test_request_returns_dict(self):
#         ngram = google_ngram.GoogleNgram()
#         ngram.set_param("content", "Albert+Einstein")
        
#         ngram.request()

#         self.assertIsInstance(ngram.data, dict)

#     def test_bad_url_raises_error(self):
#         ngram = google_ngram.GoogleNgram()
#         self.assertRaises(Exception, ngram.request_data)

#     def test_content_isnt_give(self):
#         ngram = google_ngram.GoogleNgram()
#         ngram.set_param("start_year", "2000")
        
#         self.assertRaises(Exception, ngram.request_data)

#     def test_multiple_contents_returns_each(self):
#         ngram = google_ngram.GoogleNgram()
#         ngram.set_param("content", "Albert+Einstein")
#         ngram.set_param("content", "Frankenstein")
        
#         ngram.request_data()

#         self.assertEqual(len(ngram.data), 2)

    
# if __name__ == "__main__":
#     unittest.main()