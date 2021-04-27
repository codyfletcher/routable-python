from typing import Optional

from routable.types.routable_type import RoutableType


class Membership(RoutableType):
    id: str
    email: str
    first_name: str
    last_name: str
    avatar: Optional[str]
    is_approver: bool
    is_disabled: bool

    def __init__(self, data: dict):
        self._data = data
        self.id = data["id"]
        self.email = data["attributes"]["email"]
        self.first_name = data["attributes"]["first_name"]
        self.last_name = data["attributes"]["last_name"]
        self.avatar = data["attributes"]["avatar"]
        self.is_approver = data["attributes"]["is_approver"]
        self.is_disabled = data["attributes"]["is_disabled"]

    def __str__(self):
        return f"<Membership id={self.id} first_name={self.first_name} last_name={self.last_name}>"

    def __repr__(self):
        return self.__str__()