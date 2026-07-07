from django.test import SimpleTestCase
from rest_framework.serializers import ValidationError

from shortener.validators import HttpsUrlValidator


class TestHttpsUrlValidator(SimpleTestCase):
    """
    Test HTTPS URL validation behaviour.
    """
    
    def test_https_validator_passes_for_https_url(self):
        """
        Allow URLs using the HTTPS scheme.
        """
        # Arrange
        validator = HttpsUrlValidator()

        # Act & Assert
        validator("https://example.com")  # must not raise

    def test_https_validator_raises_for_http_url(self):
        """
        Reject URLs using the HTTP scheme.
        """
        # Arrange
        validator = HttpsUrlValidator()

        # Act & Assert
        with self.assertRaises(ValidationError):
            validator("http://example.com")
    
    def test_https_validator_passes_for_none(self):
        """
        Allow None values to be handled by field-level validation.
        """
        # Arrange
        validator = HttpsUrlValidator()

        # Act & Assert
        validator(None)  # must not raise
