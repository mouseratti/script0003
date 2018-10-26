from unittest import mock
from .module1 import func1


@mock.patch("builtins.open", create=True)
def test_func1(mockedOpen):
    string,filename = 'test', 'test.txt'
    mockedFile = mock.Mock()
    mockedOpen.return_value = mockedFile
    mockedFile.__enter__ = mock.MagicMock()
    mockedFile.__exit__ = mock.MagicMock()
    mockedF = mock.Mock()
    mockedF.write.return_value = 0
    mockedFile.__enter__.return_value = mockedF
    func1(string, filename)
    mockedF.write.assert_called()
    mockedFile.__exit__.assert_called()
    # mockedOpen.assert_called_once_with(filename)