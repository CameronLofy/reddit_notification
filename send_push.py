import http.client
import urllib
from config import app_token, user_token



def send_push(message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": app_token,
            "user": user_token,
            "message": message,
            "html": 1
        }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()
