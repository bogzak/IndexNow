import requests
import json
import streamlit as st


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

        return response.status_code, response.text
