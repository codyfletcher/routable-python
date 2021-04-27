import pytest_check as check

from routable.conftest import VALID_STR, VALID_BOOL
from routable.types.membership import Membership
from routable.types.routable_type import RoutableType


class Test_Membership:
    def test__Membership__instantiation__properties_are_set(self):
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
        check.equal("https://host/image.png", sut.avatar)
        check.is_true(sut.is_approver)
        check.is_false(sut.is_disabled)

    def test__Membership__str__(self):
        data_dict = {
            "type": "Membership",
            "id": "x",
            "attributes": {
                "first_name": "y",
                "last_name": "z",
                "email": VALID_STR,
                "is_approver": VALID_BOOL,
                "is_disabled": VALID_BOOL,
                "avatar": VALID_STR,
            }
        }
        instance = Membership(data_dict)

        sut = str(instance)

        check.equal("<Membership id=x first_name=y last_name=z>", sut)

    def test__Membership__repl__matches__str__(self):
        data_dict = {
            "type": "Membership",
            "id": "x",
            "attributes": {
                "first_name": "y",
                "last_name": "z",
                "email": VALID_STR,
                "is_approver": VALID_BOOL,
                "is_disabled": VALID_BOOL,
                "avatar": VALID_STR,
            }
        }
        instance = Membership(data_dict)

        check.equal(instance.__str__(), instance.__repr__())

    def test_Membership_parent_class_is_RoutableType(self):
        data_dict = {
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
        instance = Membership(data_dict)

        assert isinstance(instance, RoutableType)