import pytest_check as check

from routable.types.membership import Membership


class Test_Membership:
    def test__Membership__instantiation_from_dict(self):
        data_dict = {
            "type": "Membership",
            "id": "660640d3-82e0-43a2-ac8a-071d63c15f54",
            "attributes": {
                "avatar": None,
                "email": "michelle@fedex.com",
                "first_name": "Michelle",
                "is_approver": True,
                "is_disabled": False,
                "last_name": "Jones"
            }
        }

        sut = Membership(data_dict)

        check.equal("660640d3-82e0-43a2-ac8a-071d63c15f54", sut.id)
        # check.equal("?????", sut.avatar)
        # check.equal("?????", sut.email)
        # check.equal("?????", sut.first_name)
        # check.equal("?????", sut.is_approver)
        # check.equal("?????", sut.is_disabled)
        # check.equal("?????", sut.last_name)