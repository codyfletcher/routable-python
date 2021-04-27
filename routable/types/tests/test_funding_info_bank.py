import pytest
import pytest_check as check

from routable.types.funding_info_bank import FundingInfoBank
from routable.types.tests.dummy import Dummy


class Test_FundingInfoBank:
    def test__instantiation__properties_are_set(self):
        data = {
            "type": "FundingInfoBank",
            "id": "abc123"
        }

        sut = FundingInfoBank(data)

        check.equal("abc123", sut.id)

    def test__str__(self):
        funding_info_bank = Dummy.funding_info_bank()
        funding_info_bank.id = "x"

        sut = str(funding_info_bank)

        check.equal("<FundingInfoBank id=x>", sut)
