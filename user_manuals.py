```python
class UserManuals:
    def __init__(self):
        self.manuals = {}

    def add_manual(self, module_name, manual_content):
        self.manuals[module_name] = manual_content

    def get_manual(self, module_name):
        return self.manuals.get(module_name, "No manual available for this module.")

    def list_all_manuals(self):
        return self.manuals.keys()


user_manuals = UserManuals()

# Add manuals for each module
user_manuals.add_manual("csv_reader", "This module is responsible for reading data from CSV files. It takes the file path as input and returns a list of dictionaries, each representing a row in the CSV file.")
user_manuals.add_manual("email_generator", "This module is responsible for generating emails. It takes investor name, investor email, and customization data as input and returns an email content.")
user_manuals.add_manual("email_sender", "This module is responsible for sending emails. It takes investor email and email content as input and sends the email.")
user_manuals.add_manual("interaction_tracker", "This module is responsible for tracking interactions. It takes investor email as input and updates the interaction status in the database.")
user_manuals.add_manual("data_storage", "This module is responsible for storing data. It takes investor email, open status, click status, response status, and customization data as input and stores them in the database.")
user_manuals.add_manual("response_logger", "This module is responsible for logging responses. It takes investor email as input and updates the response status in the database.")
user_manuals.add_manual("authentication", "This module is responsible for authenticating API calls. It uses OAuth2.0 for authentication.")
user_manuals.add_manual("data_encryption", "This module is responsible for encrypting data. It uses AES-256 encryption for all stored data.")
user_manuals.add_manual("backup_trigger", "This module is responsible for triggering backups. It triggers immediate backups for any data inconsistency.")
user_manuals.add_manual("queue_mechanism", "This module is responsible for handling rate limits on the Email API. It uses a queue mechanism to handle rate limits.")
user_manuals.add_manual("unit_tests", "This module is responsible for running unit tests for each microservice.")
user_manuals.add_manual("integration_tests", "This module is responsible for running integration tests for end-to-end workflow.")
user_manuals.add_manual("training_modules", "This module is responsible for conducting training sessions for key users.")
```