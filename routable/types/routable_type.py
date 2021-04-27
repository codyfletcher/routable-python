class RoutableType:
    id: str

    def __init__(self, data):
        self.id = data["id"]

    def __eq__(self, other):
        result = False
        if type(self) == type(other):
            if self.id == other.id:
                result = True
        return result
