import logging

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .exceptions import ShortCodeGenerationError
from .models import ShortURL
from .serializers import CreateShortURLSerializer
from .services import create_short_url

logger = logging.getLogger("application")


class ShortURLCreateView(CreateAPIView):
    """
    API end-point for creating shortened URLs.
    """

    serializer_class = CreateShortURLSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        """
        Validate an original URL, create a shortened URL entry,
        and return the generated short URL.

        Args:
            request: HTTP request containing the original URL.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response containing the generated short URL.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        original_url = serializer.validated_data["original_url"]

        try:
            short_url_obj = create_short_url(original_url)
        except ShortCodeGenerationError:
            logger.exception(f"Failed to generate short code for URL: {original_url}")
            return Response(
                {"message": "Unable to generate short URL."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        short_url = request.build_absolute_uri(
            reverse(
                "shortener:redirect-short-url",
                kwargs={"code": short_url_obj.code},
            )
        )

        logger.info(
            f"Short URL created successfully: {short_url_obj.code} -> {original_url}"
        )

        return Response(
            {
                "message": "success",
                "short_url": short_url,
            },
            status=status.HTTP_201_CREATED,
        )


class RedirectShortURLView(View):
    """
    Redirect a short URL code to its original URL.
    """

    def get(self, request: HttpRequest, code: str) -> HttpResponseRedirect:
        """
        Look up a short URL code and redirect the client.

        Args:
            request: HTTP request.
            code: Generated short URL identifier.

        Returns:
            HTTP redirect response to the original URL.
        """
        short_url = get_object_or_404(ShortURL, code=code)

        return redirect(short_url.original_url)
