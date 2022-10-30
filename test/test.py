import json
from typing import List
import google_ngram
import unittest

class TestGoogleNgramRequestOne(unittest.TestCase):

    def setUp(self) -> None:
        self.request = google_ngram.Request()

    def test_request_returns_a_list(self):
        output = self.request.request_one("Albert Einstein")

        self.assertIsInstance(output, List)

    def test_empty_request_raises_error(self):

        self.assertRaises(google_ngram.NoResultsError, self.request.request_one)
        
    def test_invalid_content_raises_error(self):

        self.assertRaises(google_ngram.NoResultsError, self.request.request_one, "asdfasdfasdf")

    def test_integer_arg_fails(self):

        self.assertRaises(TypeError, self.request.request_one, 1)

    def test_request_returns_input(self):
        output = self.request.request_one("Frankenstein")

        self.assertEqual(output[0]["ngram"], "Frankenstein")

    def test_request_fails_with_collection(self):

        self.assertRaises(TypeError, self.request.request_one,[])
        self.assertRaises(TypeError, self.request.request_one, {})
        self.assertRaises(TypeError, self.request.request_one, set())

    def test_request_case_insensitive_returns_list(self):
        self.request.set_parameter("case_insensitive", True)

        output = self.request.request_one("Albert Einstein")
        self.assertEqual(output[0]["ngram"], "Albert Einstein (All)")

    def test_improper_parameter_set(self):

        self.assertRaises(AttributeError, self.request.set_parameter, "bad_parameter", "value")
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