import string
import pandas as pd
from .pipeline_node import PipelineNode


class Cleaner(PipelineNode):
    def __init__(self, ignore_emojis=False):
        self.__ignore_emojis = ignore_emojis

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        URL_REGEX = r"(http:\/\/|https:\/\/|www\.)[a-zA-Z0-9]+(\.[a-zA-Z]+)+(/\w+)*(.\w+)*/? "
        TWITTER_URL_REGEX = r'https:\/\/t\.co\/[a-zA-Z0-9\-\.]{10}'
        MENTIONS_REGEX = r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)"
        HASHTAG_REGEX = r"#"
        EMOJIS_REGEX = r"[^A-Za-z0-9 | \n]+"
        df["text"].replace(URL_REGEX, '', regex=True, inplace=True)
        df["text"].replace(TWITTER_URL_REGEX, '', regex=True, inplace=True)
        df["text"].replace('https', '', regex=True, inplace=True)
        df["text"].replace(MENTIONS_REGEX, '', regex=True, inplace=True)
        df["text"].replace(HASHTAG_REGEX, '', regex=True, inplace=True)
        if self.__ignore_emojis:
            df["text"].replace(EMOJIS_REGEX, '', regex=True, inplace=True)
        df["text"].replace(r"\t", ' ', regex=True, inplace=True)
        df["text"].replace('[{}]'.format(string.punctuation), ' ', regex=True, inplace=True)
        df["text"].replace(r"\n", '', regex=True, inplace=True)
        df["text"] = df["text"].str.lower()
        return df
