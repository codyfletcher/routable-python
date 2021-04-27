from routable.types.tests.dummy import Dummy


class Test_RoutableType:
    def test__RoutableType__objects_considered_equal__when_class_name_and_ids_match(self):
        object_1 = Dummy.membership()
        object_1.id = "MATCH"
        object_2 = Dummy.membership()
        object_2.id = "MATCH"

        assert object_1 == object_2
