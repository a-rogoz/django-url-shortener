from rest_framework import serializers

from .validators import HttpsUrlValidator


class CreateShortURLSerializer(serializers.Serializer):
    """
    Validate input data for URL shortening requests.
    """
    
    original_url = serializers.URLField(validators=[HttpsUrlValidator()])
