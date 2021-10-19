import nltk
import pandas as pd
from .PipelineNode import PipelineNode


class Labeler(PipelineNode):
    def __init__(self):
        ...

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['labeled_text'] = df['tokenized_text'].apply(self.label)
        df['nouns'] = df['labeled_text'].apply(self.extract_nouns)
        df['adjectives'] = df['labeled_text'].apply(self.extract_adjectives)
        df['verbs'] = df['labeled_text'].apply(self.extract_verbs)
        return df

    def label(self, tokenized_tweet_text: list) -> list:
        return nltk.pos_tag(tokenized_tweet_text)

    def extract_nouns(self, labeled_text: list) -> list:
        nouns = []
        for index, value in labeled_text:
            if value in ('NNP', 'NN', 'NNS', 'NNPS'):
                nouns.append(index)
        return nouns

    def extract_verbs(self, labeled_text: list) -> list:
        verbs = []
        for index, value in labeled_text:
            if value in ('VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ'):
                verbs.append(index)
        return verbs

    def extract_adjectives(self, labeled_text: list) -> list:
        adjetives = []
        for index, value in labeled_text:
            if value in ('JJ', 'JJR', 'JJS', 'RB'):
                adjetives.append(index)
        return adjetives
