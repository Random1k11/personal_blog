"""Personal Blog Dmitry Rusanov views."""
from django.http import HttpResponse
from django.views.generic import View
from rest_framework import viewsets


class PingView(View):
    """Test if server is up."""

    def get(self, request):  # pylint: disable=unused-argument
        """Pong response."""
        return HttpResponse('pong')
