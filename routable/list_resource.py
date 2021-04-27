import requests


class ListResource:
    def __init__(self, host, headers):
        self.host = host
        self.headers = headers


class MembershipList(ListResource):
    def list(self):
        url = f"https://{self.host}/memberships/"
        response = requests.get(url, headers=self.headers, data={})
        response_dict = response.json()
        return response_dict["data"]