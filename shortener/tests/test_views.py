from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shortener.models import ShortURL


class CreateShortURLViewTests(APITestCase):
    """
    Test the API endpoint responsible for creating short URLs.
    """

    @classmethod
    def setUpTestData(cls, **kwargs):
        super().setUpTestData(**kwargs)
        cls.valid_https_url = "https://example.com"
        cls.invalid_url = "invalid-url"

    def setUp(self):
        self.url = reverse("shortener:shorten-url")
    
    def test_create_short_url(self):
        """
        Create a short URL from a valid HTTPS URL.
        """
        # Arrange & Act
        response = self.client.post(
            self.url,
            {
                "original_url": self.valid_https_url
            },
            format="json",
        )

        # Assert
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertIn(
            "short_url",
            response.data,
        )
        self.assertIn(
            "/shrt/",
            response.data["short_url"],
        )
        self.assertTrue(
            ShortURL.objects.filter(
                original_url=self.valid_https_url
            ).exists()
        )
    
    def test_rejects_invalid_url(self):
        """
        Reject requests containing invalid URL values.
        """
        # Arrange & Act
        response = self.client.post(
            self.url,
            {
                "original_url": self.invalid_url
            },
            format="json",
        )

        # Assert
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
