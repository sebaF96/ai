from .PipelineNode import PipelineNode
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

class Polarizer(PipelineNode):
    """Creo que esta clase no tiene que analizar las palabras sueltas del tokenized sino el df[text] limpio porque viene el tweet
    completo ahi, va asi lo hicimos en clase """

    def __init__(self):
        self.__analyzer = SentimentIntensityAnalyzer()

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.analyze(df)

    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        df["negative"] = ""
        df["neutral"] = ""
        df["positive"] = ""
        df["result"] = ""
        for index, row in df.iterrows():
            result = self.__analyzer.polarity_scores(row['text'])
            row["negative"] = result["neg"]
            row["neutral"] = result["neu"]
            row["positive"] = result["pos"]
            if result['compound'] >= 0.7:
                row["result"] = "Positive"
            elif result['compound'] <= 0.3:
                row["result"] = "Negative"
            else:
                row["result"] = "Neutral"
        return df