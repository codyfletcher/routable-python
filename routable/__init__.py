class MembershipList:
    def __init__(self):
        pass

    def list(self):
        return []


class Client:
    def __init__(self, authentication_token):
        pass

    @property
    def memberships(self):
        memberships = MembershipList()
        return memberships