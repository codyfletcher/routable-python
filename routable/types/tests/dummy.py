from routable.types.membership import Membership

VALID_STR = "any"
VALID_BOOL = True


class Dummy:
    @classmethod
    def membership(cls) -> Membership:
        data = {
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
        return Membership(data)
