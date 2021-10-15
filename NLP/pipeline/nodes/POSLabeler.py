import nltk
import pandas as pd
from .PipelineNode import PipelineNode


class Labeler(PipelineNode):
    def __init__(self):
        ...

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['labeled_text'] = df['tokenized_text'].apply(self.label)
        print(df)
        return df

    def label(self, tokenized_tweet_text: list) -> list:
        return nltk.pos_tag(tokenized_tweet_text)
