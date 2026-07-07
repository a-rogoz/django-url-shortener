from django.test import TestCase

from shortener.serializers import CreateShortURLSerializer


class CreateShortURLSerializerTests(TestCase):
    """
    Test validation rules for URL shortening requests.
    """

    @classmethod
    def setUpTestData(cls, **kwargs):
        super().setUpTestData(**kwargs)
        cls.valid_https_url = "https://example.com"
        cls.invalid_http_url = "http://example.com"
        cls.invalid_url = "invalid-url"

    def test_valid_https_url(self):
        """
        Accept valid HTTPS URLs.
        """
        # Arrange & Act
        serializer = CreateShortURLSerializer(
            data={"original_url": self.valid_https_url}
        )

        # Assert
        self.assertTrue(serializer.is_valid())

    def test_http_url_is_invalid(self):
        """
        Rejects URL using the HTTP scheme.
        """
        # Arrange & Act
        serializer = CreateShortURLSerializer(
            data={"original_url": self.invalid_http_url}
        )

        # Assert
        self.assertFalse(serializer.is_valid())

    def test_invalid_url_is_rejected(self):
        """
        Reject values that are not valid URLs.
        """
        # Arrange & Act
        serializer = CreateShortURLSerializer(data={"original_url": self.invalid_url})

        # Assert
        self.assertFalse(serializer.is_valid())
