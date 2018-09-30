import requests
import app_config

class Search:
    def __init__(self):
        pass

    def query(self, query):
        if query is None or not query:
            raise Exception('No query passed')

        params = {'q': query, 't': app_config.APP_NAME, 'format': 'json'}
        url = requests.get('https://api.duckduckgo.com', params=params).url
        
        r = requests.get(url)
        r.raise_for_status()
        
        return r.json()
