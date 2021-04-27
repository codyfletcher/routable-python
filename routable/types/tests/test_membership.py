import pytest_check as check

from routable.types.membership import Membership
from routable.types.tests.dummy import Dummy


class Test_Membership:
    def test__Membership__instantiation__properties_are_set(self):
        membership_dict = {
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

        sut = Membership(membership_dict)

        check.equal("abc123", sut.id)
        check.equal("email@host", sut.email)
        check.equal("first", sut.first_name)
        check.equal("last", sut.last_name)
        check.equal("https://host/image.png", sut.avatar)
        check.is_true(sut.is_approver)
        check.is_false(sut.is_disabled)

    def test__Membership__str__(self):
        membership = Dummy.membership()
        membership.id = "x"
        membership.first_name = "y"
        membership.last_name = "z"

        sut = str(membership)

        check.equal("<Membership id=x first_name=y last_name=z>", sut)
