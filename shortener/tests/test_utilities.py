from unittest.mock import patch

from django.test import SimpleTestCase

from shortener.utilities import (BASE62_ALPHABET, CODE_LENGTH,
                                 calculate_numeric_hash, encode_base62,
                                 generate_code)


class CalculateNumericHashTests(SimpleTestCase):
    """
    Test numeric hash generation.
    """

    def test_hash_is_deterministic(self):
        """
        Return the same hash for the same input.
        """
        # Arrange
        value = "https://example.com"

        # Act & Assert
        self.assertEqual(
            calculate_numeric_hash(value),
            calculate_numeric_hash(value),
        )

    def test_hash_differs_for_different_inputs(self):
        """
        Produce different hashes for different inputs.
        """
        # Act & Assert
        self.assertNotEqual(
            calculate_numeric_hash("abc123"),
            calculate_numeric_hash("def456"),
        )


class EncodeBase62Tests(SimpleTestCase):
    """
    Test Base62 encoding.
    """

    def test_encode_zero(self):
        """
        Encode zero as a padded Base62 string.
        """
        # Act & Assert
        self.assertEqual(
            encode_base62(0),
            "000000",
        )

    def test_encode_single_digit(self):
        """
        Encode a single-digit value correctly.
        """
        # Act & Assert
        self.assertEqual(
            encode_base62(1),
            "000001",
        )

    def test_returns_fixed_length_string(self):
        """
        Return a code of the configured length.
        """
        # Act
        code = encode_base62(123456)

        # Assert
        self.assertEqual(len(code), CODE_LENGTH)

    def test_contains_only_base62_characters(self):
        """
        Use only Base62 alphabet characters.
        """
        # Act
        code = encode_base62(987654)

        # Arrange
        self.assertTrue(all(char in BASE62_ALPHABET for char in code))


class GenerateCodeTests(SimpleTestCase):
    """
    Test short code generation.
    """

    def test_generate_code_returns_fixed_length(self):
        """
        Generate a code of the configured length.
        """
        # Act
        code = generate_code("https://example.com")

        # Assert
        self.assertEqual(
            len(code),
            CODE_LENGTH,
        )

    def test_generate_code_uses_base62_characters(self):
        """
        Generate a code using only Base62 characters.
        """
        # Act
        code = generate_code("https://example.com")

        # Assert
        self.assertTrue(all(char in BASE62_ALPHABET for char in code))

    @patch("shortener.utilities.time.time_ns", return_value=12345)
    def test_generate_code_is_deterministic_for_fixed_timestamp(self, mock_time_ns):
        """
        Generate the same code when given the same input and timestamp.
        """
        # Act
        code1 = generate_code("https://example.com")
        code2 = generate_code("https://example.com")

        # Assert
        self.assertEqual(code1, code2)
