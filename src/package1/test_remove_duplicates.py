import pytest
from package1.duplicates import remove_duplicates

@pytest.mark.parametrize("inp,expected", [
    ([1,2,3,3,2,1], [1,2,3]),
    ([10,9,7,10,7,9],[7,9,10]),
    ([100,100,100], 100),
])
def test_remove_duplicates(inp, expected):
    assert remove_duplicates(inp) == expected, "They are not equal!!!"