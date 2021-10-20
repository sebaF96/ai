import os
import webbrowser
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
from .PipelineNode import PipelineNode
from shutil import copyfile


class Printer(PipelineNode):
    def __init__(self):
        self.__target_directory = self.create_target_directory()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        sequence = ['nouns', 'adjectives', 'verbs', 'tokenized_text']
        df.to_csv(self.__target_directory + '/results.csv')
        self.copy_html_file()
        for sec in sequence:
            self.save_wordcloud(df, sec)
        self.save_sentiment_pie(df)
        self.save_df_as_html(df)
        # Métodos que crean gráficos aca
        webbrowser.open(self.__target_directory + '/results.html')
        return df

    def save_wordcloud(self, df: pd.DataFrame, field: str):
        wordcloud = WordCloud(
            max_words=100,
            background_color="white",
            width=800,
            height=400,
            min_word_length=2
        ).generate(df[field].to_string())
        wordcloud.to_file(self.__target_directory + f'/wc_{field}.png')

    def save_sentiment_pie(self, df: pd.DataFrame):
        result_column = df.filter(['result']).values.tolist()
        result_column = [v[0] for v in result_column]
        positives = len([r for r in result_column if r == 'Positive'])
        negatives = len([r for r in result_column if r == 'Negative'])
        neutral = len([r for r in result_column if r == 'Neutral'])
        plt.pie(
            [positives, negatives, neutral],
            colors=["#60D394", "#EE6055", "#FFD97D"],
            explode=(0.1, 0, 0),
            labels=['Positive', 'Negative', 'Neutral'],
            startangle=90,
            autopct='%1.1f%%'
        )
        plt.axis('equal')
        plt.savefig(self.__target_directory + '/sentiment.png')

    def save_df_as_html(self, df: pd.DataFrame):
        df.to_html(buf=self.__target_directory + '/df.html', columns=['text', 'tokenized_text', 'positive', 'negative',
                                                                      'neutral'])

    def copy_html_file(self):
        src = f'{pathlib.Path(__file__).parent.absolute()}/resources/results.html'
        destiny = self.__target_directory + '/results.html'
        copyfile(src, destiny)

    def create_target_directory(self) -> str:
        timestamp = int(datetime.now().timestamp())
        target_directory = f'/tmp/nlp/results_{timestamp}'
        os.makedirs(target_directory)
        return target_directory
