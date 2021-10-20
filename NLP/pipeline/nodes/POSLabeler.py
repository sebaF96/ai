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
        # Atributo de la clase -> para nouns, adjectives, verbs
        exclude = ['messi', 'mbappe', 'neymar', 'psg', 'ucl', 'nba', 'nfl', 'barca', 'uefachampions league']
        for word, tag in labeled_text:
            if tag in ('NNP', 'NN', 'NNS', 'NNPS') or word in exclude:
                nouns.append(word)
        return nouns

    def extract_verbs(self, labeled_text: list) -> list:
        verbs = []
        for word, tag in labeled_text:
            if tag in ('VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ'):
                verbs.append(word)
        return verbs

    def extract_adjectives(self, labeled_text: list) -> list:
        adjectives = []
        for word, tag in labeled_text:
            if tag in ('JJ', 'JJR', 'JJS', 'RB'):
                adjectives.append(word)
        return adjectives
