class Membership:


    def __init__(self, data: dict):
        self._data = data
        self.id = data["id"]
        self.email = data["attributes"]["email"]
        self.first_name = data["attributes"]["first_name"]
        self.last_name = data["attributes"]["last_name"]
        self.is_approver = data["attributes"]["is_approver"]
        self.is_disabled = data["attributes"]["is_disabled"]
        self.avatar = data["attributes"]["avatar"]
