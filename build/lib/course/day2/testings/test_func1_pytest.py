import pytest
from .module1 import func1


fixtures = [
    (1,1),
    (2,2),
    (3,3),
    (6,6),
    (7,6),
    (100, 6),
    (200, 6),
    (201, 8),
]


@pytest.mark.parametrize("inp, expected", fixtures)
def test_func1(inp, expected):
    assert func1(inp) == expected