import requests


class MembershipList:
    def __init__(self, headers):
        self.headers = headers

    def list(self):
        url = "https://api.sandbox.routable.com/memberships/"
        response = requests.get(url, headers=self.headers, data={})
        response_dict = response.json()
        return response_dict["data"]


class Client:
    def __init__(self, authentication_token:str):
        self.headers = {
            'Authorization': f'Bearer {authentication_token}',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

    @property
    def memberships(self):
        return MembershipList(self.headers)
