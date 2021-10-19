import string
import nltk
from nltk.tokenize import TweetTokenizer
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import pandas as pd
import os
from click import secho

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


def count_words(df):
    tokenized_list = df.explode('tokenized_text')
    fdist = FreqDist(tokenized_list['tokenized_text'])
    df_fdist = pd.DataFrame.from_dict(fdist, orient='index')
    df_fdist.columns = ['Frequency']
    df_fdist.index.name = 'Term'
    df_fdist.sort_values(by=['Frequency'], inplace=True)
    return df_fdist


def create_wordcloud(df):
    wordcloud = WordCloud(max_words=100, background_color="white").generate(df['tokenized_text'].to_string())
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.rcParams['figure.figsize'] = [150, 150]
    plt.show()


def download_packages_if_needed():
    home = os.getenv('HOME')
    if not os.path.isdir(f'{home}/nltk_data/tokenizers/punkt'):
        secho("Downloading package nltk.punkt...", fg="blue", bold=True)
        nltk.download('punkt')
    if not os.path.isdir(f'{home}/nltk_data/corpora/stopwords'):
        secho("Downloading package nltk.stopwords...", fg="blue", bold=True)
        nltk.download('stopwords')
    if not os.path.isdir(f'{home}/nltk_data/help/tagsets'):
        secho("Downloading package nltk.tagsets...", fg="blue", bold=True)
        nltk.download('tagsets')
    if not os.path.isdir(f'{home}/nltk_data/taggers/averaged_perceptron_tagger'):
        secho("Downloading package nltk.averaged_perceptron_tagger...", fg="blue", bold=True)
        nltk.download('averaged_perceptron_tagger')
    if not os.path.isdir(f'{home}/nltk_data/corpora/wordnet'):
        secho("Downloading package nltk.wordnet", fg="blue", bold=True)
        nltk.download('wordnet')
    if not os.path.isdir(f'{home}/nltk_data/sentiment/'):
        secho("Downloading package nltk.vader_lexicon", fg="blue", bold=True)
        nltk.download('vader_lexicon')
