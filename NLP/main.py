import click
from pipeline.Cleaner import Cleaner
from pipeline.Requester import Requester
from pipeline.nlp_pipeline import NLPPipeline


@click.command()
@click.option('-word', prompt=True, help="Enter a word to search", default="")
def search(word):
    click.secho("Searching tweets by specified parameters", fg="blue", bold=True)
    pipeline = NLPPipeline(word)
    pipeline.add(Requester(max_pages=3))
    pipeline.add(Cleaner(ignore_emojis=True))
    pipeline.run()

    # # Tener en cuenta los download de nltk.download()
    # # Debería poder guardar los múltiples hashtag
    # response = twitter_request(hashtag, word, bearer_token)
    # df = pd.json_normalize(response.json()['data'])
    # print(df)
    # df_clean = clean_data(df)
    # print(df_clean)
    # df_copy = df_clean
    # tokenized_df = tokenize_df(df_copy)
    # print(tokenized_df)
    # print(count_words(tokenized_df))
    # create_wordcloud(tokenized_df)


if __name__ == '__main__':
    # try:
    #     nltk.download('punkt')
    #     nltk.download('averaged_perceptron_tagger')
    #     nltk.download('wordcloud')
    #     nltk.download('stopwords')
    #     nltk.download('tagsets')
    # except Exception as e:
    #     print(e)
    #     exit(1)
    search()
