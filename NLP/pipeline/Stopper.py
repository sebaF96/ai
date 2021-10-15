from nltk.corpus import stopwords
from pipeline.PipelineNode import PipelineNode
from nltk.tokenize import word_tokenize

class Stopper(PipelineNode):
    def __init__(self):
        self.__stopwords = ''

    def handle(self, df):
        self.__stopwords = set(stopwords.words('english'))
        no_stopwords_data = []
        # Crear lista sin stopwords
        for x in df['tokenized_text']:
            for word in x:
                if word.lower() not in self.__stopwords:
                    no_stopwords_data.append(word)
        # Esta lista sin stop words deberia guardarse como df? 