from rest_framework.serializers import ValidationError


class HttpsUrlValidator:
    """
    Validator to ensure a URL uses HTTPS scheme.
    """

    https_prefix = "https://"
    message = f"URL must start with '{https_prefix}'."
    code = "invalid_scheme"

    def __call__(self, value):
        if value is None:
            return

        if not value.startswith(self.https_prefix):
            raise ValidationError(self.message, code=self.code)
