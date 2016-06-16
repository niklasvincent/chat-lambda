import json


import requests


class Slack(object):

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, text):
        """Send a message to the specified chat"""
        try:
            payload = {
                "text": text
            }
            r = requests.post(self.webhook_url, json=payload)
        except Exception as e:
            print("Failed to send Slack message: %s" % e)
