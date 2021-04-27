from routable.types.routable_type import RoutableType


class FundingInfoBank(RoutableType):
    def __init__(self, data: dict):
        super().__init__(data)

    def __str__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
