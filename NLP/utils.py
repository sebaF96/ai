url = "https://api.twitter.com/2/tweets/search/recent"
import requests
def twitter_request(hashtag, word, bearer_token) -> list:
    """ En esta funcion deberían estar los headers y los params para hacer la query en la API """
    params = {
        'query': f'{hashtag} {word}  lang:en -is:retweet',
        'tweet.fields': 'created_at',
        'max_results': 100
    }
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2FullArchiveSearchPython"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response
