import requests
import json


class IndexNow:
    def __init__(self, host, key):
        self.host = host
        self.key = key

    @staticmethod
    def get_links():
        links = []
        with open(r'urls.txt', 'r', encoding='utf-8') as file:
            for link in file:
                links.append(link.strip())
        return links

    def index_now(self):
        url = 'https://yandex.com/indexnow'
        data = {
            "host": self.host,
            "key": self.key,
            # "keyLocation": "https://www.example.com/myIndexNowKey63638.html",
            "urlList": self.get_links()
        }

        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

        response = requests.post(url, data=json.dumps(data), headers=headers)

        print(response.status_code)
        print(response.text)