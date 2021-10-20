import click
import pipeline.nodes as nd
from pipeline.nlp_pipeline import NLPPipeline
from utils import download_packages_if_needed


@click.command()
@click.option('-word', prompt=True, help="Enter a word to search", default="")
def search(word):
    sanitize_input(word)
    click.secho("Searching tweets by specified parameters", fg="blue", bold=True)
    pipeline = NLPPipeline(word)
    pipeline.add(nd.Requester(max_pages=200))
    pipeline.add(nd.Cleaner(ignore_emojis=False))
    pipeline.add(nd.Tokenizer())
    pipeline.add(nd.Stopper())
    pipeline.add(nd.Labeler())
    pipeline.add(nd.Lemmatizer())
    pipeline.add(nd.Polarizer())
    pipeline.add(nd.Printer())
    pipeline.run()


def sanitize_input(word: str):
    char_to_evaluate = word[0]
    if char_to_evaluate == '#':
        char_to_evaluate = word[1]
    if char_to_evaluate.isdigit():
        click.secho('La palabra o hashtag no puede comenzar con un número', fg='red', bold='true')
        exit(1)


if __name__ == '__main__':
    download_packages_if_needed()
    search()
