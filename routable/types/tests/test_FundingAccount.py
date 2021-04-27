import pytest
import pytest_check as check

from routable.types.FundingAccount import FundingAccount
from routable.types.tests.dummy import VALID_STR, VALID_BOOL, VALID_DATETIME_STR


class Test_FundingAccount:
    def test__instantiation__properties_are_set__from_attributes(self):
        data = {
            "type": "FundingAccount",
            "id": "abc123",
            "attributes": {
                "name": "Routable balance",
                "direction": "receivables_and_payables",
                "usable": "yes",
                "ledger_ref": None,
                "ledger_ref_payable": None,
                "ledger_ref_receivable": None,
                "is_external": False,
                "is_valid": True,
                "is_deleted": False,
                "is_disabled": False,
                "created": "2020-01-23T12:34:56.789012Z",
            },
            "relationships": {
                "address": {
                    "data": None
                },
                "balance": {
                    "data": None
                },
                "bank": {
                    "data": None
                },
                "company": {
                    "data": None
                },
                "creator": {
                    "data": None
                }
            }
        }

        sut = FundingAccount(data)

        check.equal("abc123", sut.id)
        check.equal("Routable balance", sut.name)
        check.equal("receivables_and_payables", sut.direction)
        check.equal("yes", sut.usable)
        check.is_none(sut.ledger_ref)
        check.is_none(sut.ledger_ref_payable)
        check.is_none(sut.ledger_ref_receivable)
        check.is_false(sut.is_external)
        check.is_true(sut.is_valid)
        check.is_false(sut.is_deleted)
        check.is_false(sut.is_disabled)
        check.equal("2020-01-23T12:34:56.789012Z", sut.created)

    @pytest.mark.skip("Need to figure out how we want to populate `relationships` here")
    def test__instantiation__properties_are_set__from_relationships(self):
        data = {
            "type": "FundingAccount",
            "id": "abc123",
            "attributes": {
                "name": VALID_STR,
                "direction": VALID_STR,
                "usable": VALID_STR,
                "ledger_ref": None,
                "ledger_ref_payable": None,
                "ledger_ref_receivable": None,
                "is_external": VALID_BOOL,
                "is_valid": VALID_BOOL,
                "is_deleted": VALID_BOOL,
                "is_disabled": VALID_BOOL,
                "created": VALID_DATETIME_STR,
            },
            "relationships": {
                "address": {
                    "data": None
                },
                "balance": {
                    "data": {
                        "type": "FundingInfoBalance",
                        "id": "6c9410a9-a103-4453-adba-e66859b903cd"
                    }
                },
                "bank": {
                    "data": None
                },
                "company": {
                    "data": {
                        "type": "Company",
                        "id": "9aed9792-f93c-4372-bb2d-6ae0082797db"
                    }
                },
                "creator": {
                    "data": {
                        "type": "Membership",
                        "id": "660640d3-82e0-43a2-ac8a-071d63c15f54"
                    }
                }
            }
        }

        _ = FundingAccount(data)

        assert False, "relationships not done"