import click
import pipeline.nodes as nd
from pipeline.nlp_pipeline import NLPPipeline
from utils import download_packages_if_needed


@click.command()
@click.option('-word', prompt=True, help="Enter a word to search", default="")
def search(word):
    click.secho("Searching tweets by specified parameters", fg="blue", bold=True)
    pipeline = NLPPipeline(word)
    pipeline.add(nd.Requester(max_pages=25))
    pipeline.add(nd.Cleaner(ignore_emojis=True))
    pipeline.add(nd.Tokenizer())
    pipeline.add(nd.Stopper())
    pipeline.add(nd.Labeler())
    pipeline.add(nd.Lemmatizer())
    pipeline.add(nd.Polarizer())
    pipeline.add(nd.Printer())
    pipeline.run()


if __name__ == '__main__':
    download_packages_if_needed()
    search()
