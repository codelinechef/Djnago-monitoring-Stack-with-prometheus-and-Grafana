import os
import requests

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

def send_alerts(msg: str):
    return requests.post(SLACK_WEBHOOK, json = {"text": msg})