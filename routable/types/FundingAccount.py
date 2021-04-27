from typing import Optional

from routable.types.routable_type import RoutableType


class FundingAccount(RoutableType):
    name: str
    direction: str
    usable: str
    ledger_ref: Optional[any]
    ledger_ref_payable: Optional[any]
    ledger_ref_receivable: Optional[any]
    is_external: bool
    is_valid: bool
    is_deleted: bool
    is_disabled: bool
    created: str

    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data["attributes"]["name"]
        self.direction = data["attributes"]["direction"]
        self.usable = data["attributes"]["usable"]
        self.ledger_ref = data["attributes"]["ledger_ref"]
        self.ledger_ref_payable = data["attributes"]["ledger_ref_payable"]
        self.ledger_ref_receivable = data["attributes"]["ledger_ref_receivable"]
        self.is_external = data["attributes"]["is_external"]
        self.is_valid = data["attributes"]["is_valid"]
        self.is_deleted = data["attributes"]["is_deleted"]
        self.is_disabled = data["attributes"]["is_disabled"]
        self.created = data["attributes"]["created"]
