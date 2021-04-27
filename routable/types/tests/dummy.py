from routable.types.FundingInfoBank import FundingInfoBank
from routable.types.Membership import Membership

VALID_STR = "any"
VALID_BOOL = True
VALID_DATETIME_STR = "2020-01-23T12:34:56.789012Z"


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

    @classmethod
    def funding_info_bank(cls) -> FundingInfoBank:
        data = {
            "type": "FundingInfoBank",
            "id": VALID_STR
        }
        return FundingInfoBank(data)


