"""
    conftest
    ~~~~~~~~

    High level fixtures used across multiple test modules.
"""
import os
import pytest
import random

from ulid import base32


@pytest.fixture(scope='function')
def valid_bytes_128():
    """
    Fixture that yields :class:`~bytes` instances that are 128 bits, the length of an entire ULID.
    """
    return random_bytes(16)


@pytest.fixture(scope='function')
def valid_bytes_80():
    """
    Fixture that yields :class:`~bytes` instances that are 80 bits, the length of a ULID randomness.
    """
    return random_bytes(10)


@pytest.fixture(scope='function')
def valid_bytes_48():
    """
    Fixture that yields :class:`~bytes` instances that are 48 bits, the length of a ULID timestamp.
    """
    return random_bytes(6)


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_bytes_128(request):
    """
    Fixture that yields :class:`~bytes` instances that are between 0 and 256 bits, except 128.
    """
    return random_bytes(request.param, not_in=[16])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_bytes_80(request):
    """
    Fixture that yields :class:`~bytes` instances that are between 0 and 256 bits, except 80.
    """
    return random_bytes(request.param, not_in=[10])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_bytes_48(request):
    """
    Fixture that yields :class:`~bytes` instances that are between 0 and 256 bits, except 48.
    """
    return random_bytes(request.param, not_in=[6])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_bytes_48_80_128(request):
    """
    Fixture that yields :class:`~bytes` instances that are between 0 and 256 bits, except 48, 80, and 128.
    """
    return random_bytes(request.param, not_in=[6, 10, 16])


@pytest.fixture(scope='function')
def valid_str_26():
    """
    Fixture that yields :class:`~str` instances that are 26 characters, the length of an entire ULID.
    """
    return random_str(26)


@pytest.fixture(scope='function')
def valid_str_10():
    """
    Fixture that yields :class:`~str` instances that are 10 characters, the length of a ULID timestamp.
    """
    return random_str(10)


@pytest.fixture(scope='function')
def valid_str_16():
    """
    Fixture that yields :class:`~str` instances that are 16 characters, the length of a ULID randomness.
    """
    return random_str(16)


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_str_26(request):
    """
    Fixture that yields :class:`~str` instances that are between 0 and 32 characters, except 26.
    """
    return random_str(request.param, not_in=[26])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_str_16(request):
    """
    Fixture that yields :class:`~str` instances that are between 0 and 32 characters, except 16.
    """
    return random_str(request.param, not_in=[16])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_str_10(request):
    """
    Fixture that yields :class:`~str` instances that are between 0 and 32 characters, except 10.
    """
    return random_str(request.param, not_in=[10])


@pytest.fixture(scope='function', params=range(0, 32))
def invalid_str_10_16_26(request):
    """
    Fixture that yields :class:`~str` instances that are between 0 and 32 characters, except 10, 16, and 26.
    """
    return random_str(request.param, not_in=[10, 16, 26])


def random_bytes(num_bytes, not_in=(-1,)):
    """
    Helper function that returns a number of random bytes, optionally excluding those of a specific length.
    """
    num_bytes = num_bytes + 1 if num_bytes in not_in else num_bytes
    return os.urandom(num_bytes)


def random_str(num_chars, not_in=(-1,)):
    """
    Helper function that returns a string with the specified number of random characters, optionally
    excluding those of a specific length.
    """
    num_chars = num_chars + 1 if num_chars in not_in else num_chars
    return ''.join(random.choice(base32.ENCODING) for _ in range(num_chars))