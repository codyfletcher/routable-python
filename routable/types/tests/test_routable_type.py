import pytest_check as check

from routable.types.tests.dummy import Dummy


class Test_RoutableType:
    def test__objects_considered_equal__when_class_name_and_ids_match(self):
        object_1 = Dummy.membership()
        object_2 = Dummy.membership()
        object_1.id = "MATCH"
        object_2.id = "MATCH"

        assert object_1 == object_2

    def test__objects_not_equal__when_ids_do_not_match(self):
        object_1 = Dummy.membership()
        object_2 = Dummy.membership()
        object_1.id = "Chalk"
        object_2.id = "Cheese"

        assert object_1 != object_2

    def test__objects_not_equal__when_class_names_do_not_match(self):
        object_1 = Dummy.membership()
        object_2 = Dummy.funding_info_bank()
        object_1.id = "MATCH"
        object_2.id = "MATCH"

        assert object_1 != object_2

    def test__repl__matches__str__(self):
        membership = Dummy.membership()

        check.equal(membership.__str__(), membership.__repr__())
