import time

CODE_LENGTH = 6
HASH_MULTIPLIER = 31
BASE = 62
MAX_CODE_VALUE = BASE ** CODE_LENGTH
BASE62_ALPHABET = (
    "0123456789"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
)


def generate_code(original_url: str) -> str:
    """
    Generate a short code candidate for a URL.

    Args:
        original_url: URL for which the short code is generated.

    Returns:
        Short Base62 encoded URL identifier.
    """
    timestamp = str(time.time_ns())
    value = calculate_numeric_hash(original_url + timestamp)

    return encode_base62(value, CODE_LENGTH)


def calculate_numeric_hash(value: str) -> int:
    """
    Calculate a numeric hash value from a string.

    Args:
        value: Input string to hash.
    
    Returns:
        Integer hash value.
    """
    hash_value = 0

    for char in value:
        hash_value = (hash_value * HASH_MULTIPLIER + ord(char)) % MAX_CODE_VALUE
    
    return hash_value


def encode_base62(number: int, length: int = CODE_LENGTH) -> str:
    """
    Encode an integer into a fixed-length Base62 string.

    Args:
        number: Integer value to encode.
        length: Desired length of the resulting code.
    
    Returns:
        Base62 encoded string padded to the requested length.
    """
    if number == 0:
        return BASE62_ALPHABET[0].rjust(length, "0")
    
    result = []

    while number:
        number, remainder = divmod(number, BASE)
        result.append(BASE62_ALPHABET[remainder])
    
    encoded = "".join(reversed(result))
    return encoded.rjust(length, "0")
