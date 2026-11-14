import ipaddress
import socket

from itertools import zip_longest


def scan(ip: str, port: int, timeout: int): ...


def _build_tcp_header(
    src_ip: str,
    src_port: int,
    dst_port: int,
    SYN: bool,
    ACK: bool,
    RST: bool,
    seq_num: int,
    ack_num: int,
) -> bytes: ...


def _build_pseudo_header(src_ip: str, dst_ip: str, tcp_len: int) -> bytes: ...


def _checksum16(data: bytes) -> int:
    total = 0

    for hi, lo in zip_longest(data[0::2], data[1::2], fillvalue=0):
        total += (hi << 8) + lo
        total = (total & 0xFFFF) + (total >> 16)

    return ~total & 0xFFFF


def _get_local_ip(dst_ip: str) -> str: ...


def _resolve_and_validate_target(target: str, resolver=socket.gethostbyname) -> str:
    target = target.strip()

    if not target:
        raise ValueError("Target host was empty")

    try:
        ip = ipaddress.ip_address(target)

        if ip.version == 6:
            raise ValueError("IPv6 is not supported")

        return ip.exploded

    except ValueError as e:
        if "IPv6 is not supported" in str(e):
            raise

        try:
            ip = resolver(target)
            ip = ipaddress.ip_address(ip)
            if ip.version == 6:
                raise ValueError("IPv6 is not supported")
            return ip.exploded

        except Exception:
            raise ValueError(f"Failed to resolve hostname or invalid IP: '{target}'")
