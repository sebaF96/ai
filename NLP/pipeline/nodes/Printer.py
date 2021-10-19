import os
import webbrowser
import pathlib
import pandas as pd
from wordcloud import WordCloud
from datetime import datetime
from .PipelineNode import PipelineNode
from shutil import copyfile


class Printer(PipelineNode):
    def __init__(self):
        self.__target_directory = self.create_target_directory()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_csv(self.__target_directory + '/results.csv')
        self.copy_html_file()
        self.save_wordcloud(df)
        webbrowser.open(self.__target_directory + '/results.html')
        return df

    def save_wordcloud(self, df: pd.DataFrame):
        wordcloud = WordCloud(
            max_words=100,
            background_color="white",
            width=800,
            height=400,
            min_word_length=2
        ).generate(df['tokenized_text'].to_string())
        wordcloud.to_file(self.__target_directory + '/wc.png')

    def copy_html_file(self):
        src = f'{pathlib.Path(__file__).parent.absolute()}/resources/results.html'
        destiny = self.__target_directory + '/results.html'
        copyfile(src, destiny)

    def create_target_directory(self) -> str:
        timestamp = int(datetime.now().timestamp())
        target_directory = f'/tmp/nlp/results_{timestamp}'
        os.makedirs(target_directory)
        return target_directory
