from unittest import TestCase
from .mysum import my_sum

fixtures = (
    (
        (1,2,3),
        6
    ),
    (
        (-1,1),
        0
    ),
    (
        (-1,-2),
        -3
    )


)

class TestMy_sum(TestCase):

    def test_my_sum(self):
        for fixture in fixtures:
            self.assertEqual(my_sum(*fixture[0]), fixture[1])



def test_my_sum():
    for fixture in fixtures:
        assert my_sum(*fixture[0]) == fixture[1]
