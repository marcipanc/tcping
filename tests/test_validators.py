import pytest

from scanner import _resolve_and_validate_target


@pytest.mark.parametrize(
    ("ip", "expected"),
    [
        ("192.168.1.1", "192.168.1.1"),
        ("0.0.0.0", "0.0.0.0"),
        ("255.255.255.255", "255.255.255.255"),
        ("8.8.8.8", "8.8.8.8"),
        ("  10.0.0.240  ", "10.0.0.240"),
    ],
)
def test_resolve_correct_ipv4_formats(ip, expected):
    got = _resolve_and_validate_target(ip)

    assert got == expected


def test_is_valid_port(port, expected): ...
