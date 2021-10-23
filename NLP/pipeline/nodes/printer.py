import os
import webbrowser
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
from .pipeline_node import PipelineNode
from shutil import copyfile


class Printer(PipelineNode):
    def __init__(self):
        self.__target_directory = self.create_target_directory()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        self.copy_html_file()
        df.to_csv(self.__target_directory + '/results.csv')
        sequence = ['nouns', 'adjectives', 'verbs', 'tokenized_text']
        for sec in sequence:
            self.save_wordcloud(df, sec)
        self.save_sentiment_pie(df)
        self.save_df_as_html(df)
        self.save_tweets_by_hour(df)
        self.save_tweets_by_weekday(df)
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

    def save_tweets_by_hour(self, df: pd.DataFrame):
        df_copy = df.copy()
        df_copy['created_at'] = pd.to_datetime(df_copy['created_at'], format='%Y-%m-%dT%H:%M:%S')
        groups = [df_copy['created_at'].dt.hour]
        data_hour_message = df.groupby(groups).agg(frequency=('id', 'count'))
        x = data_hour_message.index
        y = data_hour_message["frequency"]
        plt.figure(figsize=(12, 8))
        plt.xticks(list(range(24)))
        plt.bar(x, y, color='#1DA1F2')
        plt.xlabel("Hora del dia")
        plt.ylabel("Tweets")
        plt.grid(axis='y')
        plt.title("Cantidad de tweets por hora del día")
        plt.savefig(self.__target_directory + '/tbh.png')

    def save_tweets_by_weekday(self, df: pd.DataFrame):
        df_copy = df.copy()
        df_copy['created_at'] = pd.to_datetime(df_copy['created_at'], format='%Y-%m-%dT%H:%M:%S')
        groups = [df_copy['created_at'].dt.weekday]
        tweets_by_weekday = df.groupby(groups).agg(frequency=('id', 'count'))
        x = tweets_by_weekday.index
        y = tweets_by_weekday["frequency"]
        plt.figure(figsize=(12, 8))
        plt.xticks(list(range(7)), ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
        plt.bar(x, y, color='#1DA1F2')
        plt.xlabel("Día de la semana")
        plt.ylabel("Tweets")
        plt.grid(axis='y')
        plt.title("Cantidad de tweets por dia de la semana")
        plt.savefig(self.__target_directory + '/tbwd.png')

    def save_df_as_html(self, df: pd.DataFrame):
        df.head(200).to_html(
            buf=self.__target_directory + '/df.html',
            columns=['text', 'tokenized_text', 'positive', 'negative', 'neutral']
        )

    def copy_html_file(self):
        src = f'{pathlib.Path(__file__).parent.absolute()}/resources/results.html'
        destiny = self.__target_directory + '/results.html'
        copyfile(src, destiny)

    def create_target_directory(self) -> str:
        timestamp = int(datetime.now().timestamp())
        target_directory = f'/tmp/nlp/results_{timestamp}'
        os.makedirs(target_directory)
        return target_directory
