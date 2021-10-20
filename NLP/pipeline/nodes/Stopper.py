from nltk.corpus import stopwords
from .PipelineNode import PipelineNode
import pandas as pd


class Stopper(PipelineNode):
    def __init__(self):
        self.__stopwords = self.get_stopwords()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['tokenized_text'] = df['tokenized_text'].apply(self.eliminate_stopwords)
        return df

    def eliminate_stopwords(self, tokenized_tweed_text: list) -> list:
        return [word for word in tokenized_tweed_text if word not in self.__stopwords]

    def get_stopwords(self) -> list:
        stop_words = stopwords.words('english')
        new_stop_words = [
            't',
            'rt',
            'amp',
            'co'
        ]
        stop_words.extend(new_stop_words)
        return stop_words
