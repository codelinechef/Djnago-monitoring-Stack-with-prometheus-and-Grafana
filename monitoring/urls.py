# monitoring/urls.py
from django.urls import path
from .views import healthcheck, prometheusexporter, ManualAlerts

urlpatterns = [
    path("health-check/", healthcheck.as_view()),
    path("metrics/export/", prometheusexporter.as_view()),
    path("alerts/", ManualAlerts.as_view()),


]
