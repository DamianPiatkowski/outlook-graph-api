"""Module for working with Outlook through calling Graph api.

Azure app needs to be created to obtain client_id and secret (password).
Methods in this module generally modify endpoint url and adjust data format
before calling the api.
Documentation: 
https://docs.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0"""

class MailApi:
    """placeholder"""
    def __init__(self, client_id: str, password: str) -> None:
        self.client_id = client_id
        self.password = password
    
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def _call_api(self, url: str, method: str):
        pass
    
    def fetch_emails(self):
        pass