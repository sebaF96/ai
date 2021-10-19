import pandas as pd
from .PipelineNode import PipelineNode
from nltk.stem import WordNetLemmatizer


class Lemmatizer(PipelineNode):
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df2 = df.copy()
        return self.lemmatizer_fun(df2)

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


