import pytest
from unittest.mock import Mock
from package1.decorators import cacher



def test_cacher():
    io = [5,6,55,66,5,6]
    m = Mock()
    m.side_effect = io
    result = cacher(m)
    for pos in io:
        assert result(pos) == pos
        # print(m.call_count, m.call_args)
    assert m.call_count == 4

