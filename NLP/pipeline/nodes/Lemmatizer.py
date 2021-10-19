import pandas as pd
from .PipelineNode import PipelineNode
from nltk.stem import WordNetLemmatizer


class Lemmatizer(PipelineNode):
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df['nouns'] = df['nouns'].apply(self.lemmatize, args=('n',))
        df['adjectives'] = df['adjectives'].apply(self.lemmatize, args=('a',))
        df['verbs'] = df['verbs'].apply(self.lemmatize, args=('v',))
        return df

    def lemmatize(self, words: list, word_type: str):
        if word_type not in ('a', 'n', 'v', 'r'):
            raise Exception(f'LemmatizerException: word_type must be any of [a, n, v, r]. Got {word_type}')
        return [self.__lemmatizer.lemmatize(word, word_type) for word in words]

    def lemmatizer_fun(self, df: pd.DataFrame):
        for row in df['tokenized_text']:
            for word in row:
                if word in df['noun']:
                    df['tokenized_text'] = df['tokenized_text'].replace([word], self.__lemmatizer.lemmatize(word, "n"))
                elif word in df['adjective']:
                    df['tokenized_text'] = df['tokenized_text'].replace([word], self.__lemmatizer.lemmatize(word, "a"))
                elif word in df['verbs']:
                    df['tokenized_text'] = df['tokenized_text'].replace([word], self.__lemmatizer.lemmatize(word, "v"))
        return df


