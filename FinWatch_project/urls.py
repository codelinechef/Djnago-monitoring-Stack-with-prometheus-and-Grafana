"""
URL configuration for FinWatch_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from prometheus_client import make_wsgi_app
from wsgiref.util import setup_testing_defaults
from django.http import HttpResponse

def prometheus_metrics_view(request):
    from io import BytesIO
    environ = request.META.copy()
    setup_testing_defaults(environ)
    
    output = BytesIO()
    def start_response(status, headers):
        response.status_code = int(status.split(' ')[0])
        for header, value in headers:
            response[header] = value

    response = HttpResponse()
    response.status_code = 200
    app = make_wsgi_app()
    result = app(environ, start_response)
    response.content = b''.join(result)
    return response



urlpatterns = [
    path("admin/", admin.site.urls),
    path("Monitor/", include("monitoring.urls")),
    path("metrics/", prometheus_metrics_view),
]
