import requests
import json


class IndexNow:
    def __init__(self, host, key):
        self.host = host
        self.key = key

    def get_links(self, urls):
        links = []
        for link in urls:
            links.append(link.strip())
        return links

    def index_now(self, urls):
        url = 'https://yandex.com/indexnow'
        data = {
            "host": self.host,
            "key": self.key,
            # "keyLocation": "https://www.example.com/myIndexNowKey63638.html",
            "urlList": self.get_links(urls)
        }

        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)

        http_code = response.status_code
        response_text = response.text

        if http_code == 200:
            reason_text = "✅ URLs successfully sent"
        elif http_code == 202:
            reason_text = "⏳ URLs received. Pending IndexNow key verification."
        elif http_code == 400:
            reason_text = "❌ Invalid format"
        elif http_code == 403:
            reason_text = "🔑 Invalid or missing key"
        elif http_code == 422:
            reason_text = "🚫 URLs does not belong to host or key does not match protocol schema"
        elif http_code == 429:
            reason_text = "🚨 Too many requests (potential spam)"
        else:
            reason_text = f"❓ Unknown error"

        return http_code, response_text, reason_text