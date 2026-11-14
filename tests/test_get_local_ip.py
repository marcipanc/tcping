import pytest

from mock import patch
from src.scanner import _get_local_ip


@pytest.mark.parametrize(
    ("dst_ip", "expected"),
    [("127.0.0.1", "127.0.0.1"), ("localhost", "127.0.0.1"), ("1.1.1.1", "1.2.3.4")],
)
def test_get_local_ip(dst_ip, expected):

    with patch("socket.socket.getsockname") as sock_mock:
        sock_mock.return_value = (expected, 0)
        got = _get_local_ip(dst_ip)

    assert got == expected
