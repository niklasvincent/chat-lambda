import urllib
import requests


class Telegram(object):

    def __init__(self, api_key, chat_id, parse_mode="html"):
        self.api_key = str(api_key)
        self.base_url = "https://api.telegram.org/bot%s" % self.api_key
        self.chat_id = str(chat_id)
        self.parse_mode = parse_mode

    def send_message(self, text):
        """Send a message to the specified group"""
        try:
            payload = urllib.urlencode({
                    'chat_id': self.chat_id,
                    'text': text.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'parse_mode': self.parse_mode
            })
            url = self.base_url + "/sendMessage"
            r = requests.get(url, params=payload)
        except Exception as e:
            print("Failed to send Telegram message to %s: %s" % (chat_id, e))
