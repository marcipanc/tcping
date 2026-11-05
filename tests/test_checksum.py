import pytest

from src.scanner import _checksum16


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", 0xFFFF),
        (b"\x01", 0xFEFF),
        (b"\xff\xff", 0x0000),
        (b"\x04\x02\xff", 0xFCFC),
        (b"\x01\x02\xfe\xfd", 0x0000),
        (b"\xff\xff\x00\x01", 0xFFFE),
        (
            b"\x45\x00\x00\x2c\xab\xcd\x40\x00\x40\x06\x00\x00\x0a\x00\x00\x01\x0a\x00\x00\x02",
            0x7AFC,
        ),
    ],
)
def test_computes_correctly(data, expected):
    got = _checksum16(data)

    assert got == expected
