from django.db import IntegrityError

from .exceptions import ShortCodeGenerationError
from .models import ShortURL
from .utilities import generate_code

MAX_ATTEMPTS = 5


def create_short_url(original_url: str) -> ShortURL:
    """
    Create a shortened URL object.

    Args:
        original_url: URL to be shortened.

    Returns:
        Created ShortURL instance.
    """
    for _ in range(MAX_ATTEMPTS):
        code = generate_code(original_url)

        if not ShortURL.objects.filter(code=code).exists():
            try:
                return ShortURL.objects.create(
                    original_url=original_url,
                    code=code,
                )
            except IntegrityError:
                continue

    raise ShortCodeGenerationError("Unable to generate unique short code.")
