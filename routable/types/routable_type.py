class RoutableType:
    id: str

    def __init__(self, data):
        self.id = data["id"]

    def __eq__(self, other):
        classes_match = type(self) == type(other)
        ids_match = self.id == other.id
        return classes_match and ids_match

    def __repr__(self):
        return self.__str__()
