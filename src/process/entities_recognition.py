import spacy

# identifica las entidades de un articulo.
# TODO implementar
class NLP:
    def __init__(self):
        self.nlp = spacy.load('es-core-news-md')


def identify(text):
    return text