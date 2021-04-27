import pytest_check as check

from routable.conftest import dummy_membership_dict
from routable.types.membership import Membership
from routable.types.routable_type import RoutableType


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
        membership_dict = dummy_membership_dict()
        membership_dict["id"] = "x"
        membership_dict["attributes"]["first_name"] = "y"
        membership_dict["attributes"]["last_name"] = "z"
        instance = Membership(membership_dict)

        sut = str(instance)

        check.equal("<Membership id=x first_name=y last_name=z>", sut)

    def test__Membership__repl__matches__str__(self):
        membership_dict = dummy_membership_dict()
        membership_dict["id"] = "x"
        membership_dict["attributes"]["first_name"] = "y"
        membership_dict["attributes"]["last_name"] = "z"

        instance = Membership(membership_dict)

        check.equal(instance.__str__(), instance.__repr__())

    def test_Membership_parent_class_is_RoutableType(self):
        membership_dict = dummy_membership_dict()
        instance = Membership(membership_dict)

        assert isinstance(instance, RoutableType)
