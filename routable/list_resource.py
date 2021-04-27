from typing import List

import requests

from routable.types.membership import Membership


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
    def list(self) -> List[Membership]:
        response_dict = self.content_from_endpoint("memberships/")
        result = []
        for x in response_dict["data"]:
            result.append(Membership(x))
        return result
