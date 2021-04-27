from routable.conftest import dummy_membership
from routable.types.membership import Membership


class Dummy:
    @classmethod
    def membership(self) -> Membership:
        return dummy_membership()