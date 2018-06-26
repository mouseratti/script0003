import pytest
from homeworks.hw1 import flatten_list2



@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1,[2,[3,4]],5,[6,]], [1,2,3,4,5,6])
])
def test_flatten_list2(inp, expected):
    assert flatten_list2(inp) == expected
