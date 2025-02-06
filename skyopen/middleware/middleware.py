from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False) and not request.user.is_staff:
            return render(request, 'maintenance.html', status=503)

        response = self.get_response(request)

        return response
