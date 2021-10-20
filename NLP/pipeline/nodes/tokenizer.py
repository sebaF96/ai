from .pipeline_node import PipelineNode
from nltk.tokenize import TweetTokenizer


class Tokenizer(PipelineNode):
    def __init__(self):
        self.__tt = TweetTokenizer()

    def handle(self, df):
        tokenized_text = df['text'].apply(self.__tt.tokenize)
        df["tokenized_text"] = tokenized_text
        return df
