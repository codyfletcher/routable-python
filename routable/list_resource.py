import requests


class ListResource:
    def __init__(self, host, headers):
        self.host = host
        self.headers = headers

    def content_from_endpoint(self, endpoint):
        url = f"https://{self.host}/{endpoint}"
        response = requests.get(url, headers=self.headers, data={})
        response_dict = response.json()
        return response_dict


class MembershipList(ListResource):
    def list(self):
        response_dict = self.content_from_endpoint("memberships/")
        result = response_dict["data"]
        return result
