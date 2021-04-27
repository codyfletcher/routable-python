import pytest_check as check

from routable.types.membership import Membership


class Test_Membership:
    def test__Membership__instantiation_from_dict(self):
        data_dict = {
            "type": "Membership",
            "id": "abc123",
            "attributes": {
                "email": "email@host",
                "first_name": "first",
                "last_name": "last",
                "is_approver": True,
                "is_disabled": False,
                "avatar": "https://host/image.png",
            }
        }

        sut = Membership(data_dict)

        check.equal("abc123", sut.id)
        check.equal("email@host", sut.email)
        check.equal("first", sut.first_name)
        check.equal("last", sut.last_name)
        check.is_true(sut.is_approver)
        check.is_false(sut.is_disabled)
        check.equal("https://host/image.png", sut.avatar)
