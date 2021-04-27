from routable.list_resource import MembershipList


class Client:
    def __init__(self, authentication_token:str):
        self.host = "api.sandbox.routable.com"
        self.headers = {
            'Authorization': f'Bearer {authentication_token}',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

    @property
    def memberships(self):
        return MembershipList(self.host, self.headers)
