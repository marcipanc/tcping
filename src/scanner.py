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


def _calculate_checksum(data: bytes) -> int: ...


def _get_local_ip(dst_ip: str) -> str: ...


def _is_valid(ip: str) -> bool: ...
