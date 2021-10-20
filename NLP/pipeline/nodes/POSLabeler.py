import nltk
import pandas as pd
from .PipelineNode import PipelineNode


class Labeler(PipelineNode):
    def __init__(self):
        self.__known_nouns = ['messi', 'mbappe', 'neymar', 'psg', 'ucl', 'nba', 'nfl', 'barca', 'uefachampions league']
        self.__known_verbs = []
        self.__known_adjectives = ['goat']

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['labeled_text'] = df['tokenized_text'].apply(self.label)
        df['nouns'] = df['labeled_text'].apply(self.extract_nouns)
        df['adjectives'] = df['labeled_text'].apply(self.extract_adjectives)
        df['verbs'] = df['labeled_text'].apply(self.extract_verbs)
        return df

    def label(self, tokenized_tweet_text: list) -> list:
        return nltk.pos_tag(tokenized_tweet_text)

    def extract_nouns(self, labeled_text: list) -> list:
        def is_noun(word: str, tag: str) -> bool:
            if word in self.__known_verbs or word in self.__known_adjectives:
                return False
            return tag in ('NNP', 'NN', 'NNS', 'NNPS') or word in self.__known_nouns
        return [word for word, tag in labeled_text if is_noun(word, tag)]

    def extract_verbs(self, labeled_text: list) -> list:
        def is_verb(word: str, tag: str) -> bool:
            if word in self.__known_nouns or word in self.__known_adjectives:
                return False
            return tag in ('VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ') or word in self.__known_verbs
        return [word for word, tag in labeled_text if is_verb(word, tag)]

    def extract_adjectives(self, labeled_text: list) -> list:
        def is_adjective(word: str, tag: str) -> bool:
            if word in self.__known_nouns or word in self.__known_verbs:
                return False
            return tag in ('JJ', 'JJR', 'JJS', 'RB') or word in self.__known_adjectives
        return [word for word, tag in labeled_text if is_adjective(word, tag)]
