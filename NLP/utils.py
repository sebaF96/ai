import nltk
import os
from click import secho


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
