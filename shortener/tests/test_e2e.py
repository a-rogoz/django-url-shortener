from django.test import TestCase
from django.urls import reverse


class URLShortenerE2ETests(TestCase):
    """
    Test the complete URL shortening workflow.
    """

    @classmethod
    def setUpTestData(cls, **kwargs):
        super().setUpTestData(**kwargs)
        cls.valid_https_url = "https://example.com"

    def test_complete_shortening_flow(self):
        """
        Create a short URL and redirect to the original URL.
        """
        # Arrange & Act
        create_response = self.client.post(
            reverse("shortener:shorten-url"),
            {
                "original_url": self.valid_https_url
            },
            content_type="application/json",
        )

        # Assert create response
        self.assertEqual(
            create_response.status_code,
            201,
        )

        # Arrange
        short_url = create_response.json()["short_url"]

        # Assert short URL
        self.assertIn(
            "/shrt/",
            short_url,
        )

        # Act
        redirect_response = self.client.get(short_url)

        # Assert redirect response
        self.assertEqual(redirect_response.status_code, 302)
        self.assertEqual(redirect_response.url, self.valid_https_url)