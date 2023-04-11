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

        http_code = response.status_code
        response_text = response.text

        if http_code == 200:
            print("Response - OK, Reason - URL successfully sent")
        elif http_code == 202:
            print("Response - Received, Reason - URL received. Pending IndexNow key verification.")
        elif http_code == 400:
            print("Response - Bad request, Reason - Invalid format")
        elif http_code == 403:
            print("Response - Prohibited, Reason - Invalid or missing key")
        elif http_code == 422:
            print("Response - Unprocessed Entity, Reason - URL does not belong to the host or key does not match the protocol scheme")
        elif http_code == 429:
            print("Response - Too Many Requests, Reason - Too many requests (potential spam)")
        else:
            print(f"Unknown error. HTTP code: {http_code}, response text: {response_text}")
