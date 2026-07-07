from unittest.mock import patch

from django.test import TestCase

from shortener.exceptions import ShortCodeGenerationError
from shortener.models import ShortURL
from shortener.services import create_short_url

EXAMPLE_CODE_1 = "abc123"
EXAMPLE_CODE_2 = "def456"


class CreateShortURLServiceTests(TestCase):
    """
    Test URL shortening service behaviour.
    """

    @classmethod
    def setUpTestData(cls, **kwargs):
        super().setUpTestData(**kwargs)
        cls.valid_https_url = "https://example.com"
        cls.existing_url = "https://existing.com"

    def test_creates_short_url(self):
        """
        Create a ShortURL object for a valid URL.
        """
        # Act
        result = create_short_url(
            self.valid_https_url
        )

        # Assert
        self.assertEqual(
            result.original_url,
            self.valid_https_url,
        )
        self.assertIsNotNone(result.code)
        self.assertTrue(
            ShortURL.objects.filter(
                original_url=self.valid_https_url
            ).exists()
        )
    
    @patch(
            "shortener.services.generate_code",
            side_effect=[
                EXAMPLE_CODE_1,
                EXAMPLE_CODE_2,
            ]        
    )
    def test_generates_unique_code(self, mock_generate_code):
        """
        Retry code generation when a collision occurs.
        """
        # Arrange
        ShortURL.objects.create(
            original_url=self.existing_url,
            code=EXAMPLE_CODE_1,
        )

        # Act
        result = create_short_url(
            self.valid_https_url
        )

        # Assert
        self.assertEqual(
            result.code,
            EXAMPLE_CODE_2,
        )
    
    @patch("shortener.services.generate_code", return_value=EXAMPLE_CODE_1)
    def test_raises_when_code_generation_fails(self, mock_generate_code):
        """
        Raise an exception when a unique code cannot be generated.
        """
        # Arrange
        ShortURL.objects.create(
            original_url=self.existing_url,
            code=EXAMPLE_CODE_1,
        )

        # Act & Assert
        with self.assertRaises(ShortCodeGenerationError):
            create_short_url(self.valid_https_url)
