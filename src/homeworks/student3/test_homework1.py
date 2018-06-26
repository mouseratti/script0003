import pytest
from homeworks.student3 import flatten_list2, flatten_nested_list



@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1,[2,[3,4]],5,[6,]], [1,2,3,4,5,6])
])
def test_flatten_list2(inp, expected):
    assert flatten_list2(inp) == expected




@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1,[2,[3,4]],5,[6,]], [1,2,3,4,5,6])
    ])
def test_flatten_list(inp, expected):
    assert flatten_nested_list(inp) == expected




