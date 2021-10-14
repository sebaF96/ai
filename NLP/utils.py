import string
from nltk.tokenize import TweetTokenizer
import requests

url = "https://api.twitter.com/2/tweets/search/recent"

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

def clean_data(df: list) -> list:
    """Esta función recibe el dataframe y le quita las menciones, urls hashtags y simbolos raros, deja emojis(requisito)"""
    URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    MENTIONS_REGEX = r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
    HASHTAG_REGEX = r"#"

    df["text"].replace(URL_REGEX, '', regex=True, inplace=True)
    df["text"].replace(MENTIONS_REGEX, '', regex=True, inplace=True)
    df["text"].replace(HASHTAG_REGEX, '', regex=True, inplace=True)
    # df["text"].replace(r"[^A-Za-z0-9 | \n]+", ' ', regex=True, inplace=True) Esta linea quita emojis
    df["text"].replace(r"\t", ' ', regex=True, inplace=True)
    df["text"].replace('[{}]'.format(string.punctuation), ' ', regex=True, inplace=True)
    df["text"].replace(r"\n", '', regex=True, inplace=True)
    df["text"] = df["text"].str.lower()

    return df

def tokenize_df(df: list) -> list:
    tt = TweetTokenizer()
    tokenized_text = df['text'].apply(tt.tokenize)
    df["tokenized_text"] = tokenized_text
    return df