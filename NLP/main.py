import click
from pipeline.nlp_pipeline import NLPPipeline
from pipeline.nodes import *
from pipeline.nodes.Tokenizer import Tokenizer
from utils import download_packages_if_needed


@click.command()
@click.option('-word', prompt=True, help="Enter a word to search", default="")
def search(word):
    click.secho("Searching tweets by specified parameters", fg="blue", bold=True)
    pipeline = NLPPipeline(word)
    pipeline.add(Requester(max_pages=5))
    pipeline.add(Cleaner(ignore_emojis=True))
    pipeline.add(Tokenizer())
    pipeline.add(Stopper())
    pipeline.add(Labeler())
    pipeline.add(Lemmatizer())
    pipeline.add(Polarizer())
    pipeline.run()


if __name__ == '__main__':
    download_packages_if_needed()
    search()
