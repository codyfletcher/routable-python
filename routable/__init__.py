class MembershipList:
    def __init__(self):
        pass

    def list(self):
        return []


class Client:
    def __init__(self, authentication_token):
        self.headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

    @property
    def memberships(self):
        memberships = MembershipList()
        return memberships