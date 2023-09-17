```python
import csv
import json

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        data = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                investor_name = row[0]
                investor_email = row[1]
                customization_data = json.loads(row[2])
                data.append({
                    'InvestorName': investor_name,
                    'InvestorEmail': investor_email,
                    'CustomizationData': customization_data
                })
        return data

# Usage
# csv_reader = CSVReader('investors.csv')
# data = csv_reader.read_csv()
# print(data)
```