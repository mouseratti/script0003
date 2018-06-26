import pytest
from unittest.mock import Mock
from package1.generators import (
    gen1,
    fib_gen2,
)



def test_gen1():
    io = [1,2,3,4,5]
    m = Mock()
    m.side_effect = io
    g = gen1(m, io)
    counter = 0
    with pytest.raises(StopIteration):
        while 1:
            next(g)
            counter+=1
            assert counter == m.call_count




def test_fib_gen2():
    g = fib_gen2(10)
    l = next(g)
    l.append(100)
    l2 = next(g)
    assert len(l2) == 3