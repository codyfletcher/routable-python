import json

from routable.types.membership import Membership

VALID_STR = "any"
VALID_BOOL = True


class MockResponse:
    def __init__(self, response_json_str, status_code):
        self.response_json_str = response_json_str
        self.status_code = status_code

    def json(self):
        return json.loads(self.response_json_str)


def dummy_membership() -> Membership:
    membership_dict = {
        "type": "Membership",
        "id": VALID_STR,
        "attributes": {
            "first_name": VALID_STR,
            "last_name": VALID_STR,
            "email": VALID_STR,
            "is_approver": VALID_BOOL,
            "is_disabled": VALID_BOOL,
            "avatar": VALID_STR,
        }
    }
    return Membership(membership_dict)
