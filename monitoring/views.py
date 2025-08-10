from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from monitoring.utils.system_monitor import get_system_health
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from django.http import HttpResponse
from monitoring.metrics.prometheus_exporter import update_metrics
from monitoring.alerts.slack_alerts import send_alerts


class healthcheck(APIView):
    def get(self, request):
        return Response(get_system_health())
    
class prometheusexporter(APIView):
    def get(self, request):
        update_metrics()
        return HttpResponse(generate_latest(), content_type = CONTENT_TYPE_LATEST)
    
class ManualAlerts(APIView):
    def post(self, request):
        message = request.data.get("message")
        send_alerts(message)

        return Response({"status": "alert sent"})
