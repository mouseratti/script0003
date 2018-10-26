from unittest import mock
from course.day2.mocking import A, B, C
import pytest
from subprocess import TimeoutExpired

_returned = 555555

# def test_classA():
#     b = B()
#     a = A(b)
#     with pytest.raises(TimeoutExpired):
#         a.get_param1_value()
def testlist():
    assert [1,2,3] == [3,2,1]



def test_classA_with_mock():
    b = mock.Mock(B)
    b.get_value.side_effect = [0, TimeoutExpired("ping ya.ru", 5)]
    a = A(b)
    assert a.get_param1_value() == 0
    with pytest.raises(TimeoutExpired):
        a.get_param1_value()



def test_classC_with_context():
    with mock.patch("course.day2.mocking.class_c.B") as MockedB:
        b = mock.Mock()
        MockedB.return_value = b
        b.get_value.return_value = _returned
        c = C()
        assert c.get_param1_value() == _returned
        b.get_value.assert_called_once()
        b.get_value.assert_called_with(c)


@mock.patch("course.day2.mocking.class_c.B")
def test_classA_with_mock_patch(MockedB):
    b = mock.Mock()
    MockedB.return_value = b
    b.get_value.return_value = _returned
    c = C()
    assert c.get_param1_value() == _returned
    assert b.get_value.call_count == 1
    b.get_value.assert_called_with(c)


