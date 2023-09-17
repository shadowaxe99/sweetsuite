import unittest
from csv_reader import CsvReader
from email_generator import EmailGenerator
from email_sender import EmailSender
from interaction_tracker import InteractionTracker
from data_storage import DataStorage
from response_logger import ResponseLogger

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.csv_reader = CsvReader()
        self.email_generator = EmailGenerator()
        self.email_sender = EmailSender()
        self.interaction_tracker = InteractionTracker()
        self.data_storage = DataStorage()
        self.response_logger = ResponseLogger()

    def test_end_to_end(self):
        # Read data from CSV
        data = self.csv_reader.read_csv('investor_data.csv')

        for row in data:
            # Generate email
            email_content = self.email_generator.generate_email(row['InvestorName'], row['CustomizationData'])

            # Send email
            self.email_sender.send_email(row['InvestorEmail'], email_content)

            # Track interaction
            self.interaction_tracker.track_interaction(row['InvestorEmail'])

            # Store data
            self.data_storage.store_data(row['InvestorEmail'], 'OpenStatus', 'ClickStatus', 'ResponseStatus', row['CustomizationData'])

            # Log response
            self.response_logger.log_response(row['InvestorEmail'])

if __name__ == '__main__':
    unittest.main()