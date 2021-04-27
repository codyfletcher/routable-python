import pytest_check as check

from routable.types.FundingInfoBank import FundingInfoBank


class Test_FundingInfoBank:
    def test__instantiation__properties_are_set(self):
        data = {
            "type": "FundingInfoBank",
            "id": "abc123"
        }

        sut = FundingInfoBank(data)

        check.equal("abc123", sut.id)

