import requests
import app_config

class DDGSearch:
    def __init__(self):
        pass

    def query(self, query):
        params = {'q': query, 't': app_config.APP_NAME, 'format': 'json'}
        url = requests.get('https://api.duckduckgo.com', params=params).url
        print(url)
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
