```python
import requests
from authentication import get_auth_token

def send_email(investor_name, investor_email, email_content, customization_data):
    url = "http://api.emailservice.com/sendEmail"
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_auth_token()
    }
    data = {
        "InvestorName": investor_name,
        "InvestorEmail": investor_email,
        "EmailContent": email_content,
        "CustomizationData": customization_data
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Request to {url} failed with status code {response.status_code}.")
    
    return response.json()
```