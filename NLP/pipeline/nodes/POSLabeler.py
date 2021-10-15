import nltk
import pandas as pd
from .PipelineNode import PipelineNode


class Labeler(PipelineNode):
    def __init__(self):
        ...

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['labeled_text'] = df['tokenized_text'].apply(self.label)
        df['noun'] = df['labeled_text'].apply(self.order_nouns)
        df['adjective'] = df['labeled_text'].apply(self.order_adjectives)
        df['verbs'] = df['labeled_text'].apply(self.order_verbs)
        return df

    def label(self, tokenized_tweet_text: list) -> list:
        return nltk.pos_tag(tokenized_tweet_text)

    def order_nouns(self, labeled_text: list) -> list:
        nouns = []
        for index, value in labeled_text:
            if value == 'NNP' or value == 'NN':
                nouns.append(index)
        return nouns

    def order_verbs(self, labeled_text: list) -> list:
        verbs = []
        for index, value in labeled_text:
            if value == 'VB':
                verbs.append(index)
            return verbs

    def order_adjectives(self, labeled_text: list) -> list:
        adjetives = []
        for index, value in labeled_text:
            if value == 'JJ' or value == 'RB':
                adjetives.append(index)
            return adjetives
