import click
import os
from dotenv import load_dotenv
import pandas as pd
from utils import twitter_request, url

@click.command()
@click.option('-hashtag', prompt=True, help="Enter a hashtag to search with #", default="")
@click.option('-word', prompt=True, help="Enter a word to search", default="")
def search(hashtag, word):
    load_dotenv()
    # Cargar valor del token a variable
    bearer_token = os.environ.get("BEARER_TOKEN")
    click.secho("Searching tweets by specified parameters", fg="blue", bold=True)
    # Tener en cuenta los download de nltk.download()
    # Debería poder guardar los múltiples hashtag
    response = twitter_request(hashtag, word, bearer_token)
    df = pd.json_normalize(response.json()['data'])
    print(df)

if __name__ == '__main__':
    search()