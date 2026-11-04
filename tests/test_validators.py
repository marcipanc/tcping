import pytest

from src.scanner import _resolve_and_validate_target


def failing_dns(hostname):
    raise OSError()


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


@pytest.mark.parametrize(
    "ip",
    [
        ("some data"),
        ("256.100.50.1"),
        ("-1.10.10.23"),
        ("192.168.1"),
        ("abc.def.ghi.jkl"),
        ("2001:DB8::A1B2"),
    ],
)
def test_raises_exception_when_incorrect_ip(ip):
    with pytest.raises(ValueError):
        _resolve_and_validate_target(ip, resolver=failing_dns)


@pytest.mark.parametrize(
    ("domain, expected"),
    [
        ("localhost", "127.0.0.1"),
        ("ya.ru", "77.88.55.242"),
        ("www.urfu.ru", "93.88.179.201"),
        ("  localhost ", "127.0.0.1"),
        (" google.com  ", "64.233.163.101"),
    ],
)
def test_resolve_correct_domains(domain, expected):
    fake_dns = lambda hotname: expected

    got = _resolve_and_validate_target(domain, resolver=fake_dns)

    assert got == expected


@pytest.mark.parametrize(
    "domain",
    [
        ("some data"),
        ("google..com"),
        ("goo gle.com"),
        ("://google.com"),
        ("google@com"),
    ],
)
def test_raises_exception_when_incorrect_domain(domain):
    with pytest.raises(ValueError):
        _resolve_and_validate_target(domain, resolver=failing_dns)
