from pipeline.PipelineNode import PipelineNode
from nltk.tokenize import TweetTokenizer

class Tokenizer(PipelineNode):
    def __init__(self):
        self.__tt = TweetTokenizer()


    def handle(self, df):
        tt = self.__tt
        tokenized_text = df['text'].apply(tt.tokenize)
        df["tokenized_text"] = tokenized_text
        return df




