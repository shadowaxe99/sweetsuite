import unittest
from csv_reader import CsvReader
from email_generator import EmailGenerator
from email_sender import EmailSender
from interaction_tracker import InteractionTracker
from data_storage import DataStorage
from response_logger import ResponseLogger

class TestMicroservices(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CsvReader()
        self.email_generator = EmailGenerator()
        self.email_sender = EmailSender()
        self.interaction_tracker = InteractionTracker()
        self.data_storage = DataStorage()
        self.response_logger = ResponseLogger()

    def test_csv_reader(self):
        data = self.csv_reader.read_csv('investors.csv')
        self.assertIsNotNone(data)

    def test_email_generator(self):
        email_content = self.email_generator.generate_email('investor1', 'investor1@example.com', 'custom_data')
        self.assertIsNotNone(email_content)

    def test_email_sender(self):
        response = self.email_sender.send_email('investor1@example.com', 'email_content')
        self.assertEqual(response.status_code, 200)

    def test_interaction_tracker(self):
        response = self.interaction_tracker.track_interaction('investor1@example.com')
        self.assertEqual(response.status_code, 200)

    def test_data_storage(self):
        response = self.data_storage.store_data('investor1@example.com', 'open_status', 'click_status', 'response_status', 'custom_data')
        self.assertEqual(response.status_code, 200)

    def test_response_logger(self):
        response = self.response_logger.log_response('investor1@example.com', 'response_status')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()