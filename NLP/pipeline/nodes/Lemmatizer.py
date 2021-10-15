import pandas as pd
from .PipelineNode import PipelineNode
from nltk.stem import WordNetLemmatizer
from utils import create_wordcloud

class Lemmatizer(PipelineNode):
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        ...
        
    def lemmatizer(self, df: pd.DataFrame):
        for row in df['tokenized_text']:
            print("fila+1")
            for word in row:
                if word in df['noun']:
                    print(word)
                    df['tokenized_text'][word] = self.__lemmatizer.lemmatize(word, "n")
                elif word in df['adjective']:
                    df['tokenized_text'][word] = self.__lemmatizer.lemmatize(word, "a")
                elif word in df['verbs']:
                    df['tokenized_text'][word] = self.__lemmatizer.lemmatize(word, "v")
        return df


