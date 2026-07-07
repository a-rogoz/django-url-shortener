from django.test import TestCase
from django.urls import reverse

from shortener.models import ShortURL


class RedirectShortURLViewTests(TestCase):
    """
    Test redirect behaviour for generated short URLs.
    """

    @classmethod
    def setUpTestData(cls, **kwargs):
        super().setUpTestData(**kwargs)
        cls.valid_https_url = "https://example.com"

    def test_redirects_to_original_url(self):
        """
        Redirect an existing short code to its original URL.
        """
        # Arrange
        short_url = ShortURL.objects.create(
            original_url=self.valid_https_url,
            code="abc123",
        )

        # Act
        response = self.client.get(
            reverse(
                "shortener:redirect-short-url",
                kwargs={
                    "code": short_url.code,
                },
            )
        )

        # Assert
        self.assertEqual(
            response.status_code,
            302,
        )
        self.assertEqual(
            response.url,
            self.valid_https_url,
        )
    
    def test_unknown_code_returns_404(self):
        """
        Return 404 when the requested short code does not exist.
        """
        # Act
        response = self.client.get(
            reverse(
                "shortener:redirect-short-url",
                kwargs={
                    "code": "def456",
                },
            )
        )

        # Assert
        self.assertEqual(
            response.status_code,
            404,
        )
