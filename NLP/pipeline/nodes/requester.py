import click
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from .pipeline_node import PipelineNode


class Requester(PipelineNode):
    def __init__(self, max_pages=10):
        self.__words = ''
        self.__url = "https://api.twitter.com/2/tweets/search/recent"
        self.__max_pages = max_pages
        load_dotenv()

    def handle(self, words):
        self.__words = words
        bearer_token = os.getenv('BEARER_TOKEN')
        params = {
            'query': f'{self.__words}  lang:en -is:retweet -has:links',
            'tweet.fields': 'created_at',
            'max_results': 100
        }
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "User-Agent": "v2FullArchiveSearchPython"
        }
        response = requests.get(self.__url, headers=headers, params=params)
        results = list((response.json()['data']))
        token = response.json()['meta']['next_token'] if 'next_token' in response.json()['meta'] else None
        requests_made = 1
        while token and requests_made < self.__max_pages:
            params['next_token'] = response.json()['meta']['next_token']
            response = requests.get(self.__url, headers=headers, params=params)
            requests_made += 1
            results.extend(response.json()['data'])
            token = response.json()['meta']['next_token'] if 'next_token' in response.json()['meta'] else None
        results = pd.DataFrame(results)
        click.secho(f"Found {len(results)} tweets", fg="green", bold=True)
        return results
