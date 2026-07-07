from django.db import models

CODE_LENGTH = 6


class ShortURL(models.Model):
    """
    Store mappings between original URLs and generated short codes.
    """

    original_url = models.URLField(max_length=2048)
    code = models.CharField(max_length=CODE_LENGTH, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"

    def __str__(self) -> str:
        return f"{self.code}: {self.original_url[:50]}"
