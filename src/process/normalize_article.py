import re
import spacy
from pathlib import Path
from spacy import displacy
from src.models.article import get_articles, update_html_article


# limpia el articulo para facilitar la identificacion de entidades.
def normalize(text):
    nlp = spacy.load('es_core_news_md')
    text_normalized = text

    if search_pattern(text):
        print("entro el id del search patter")
        text_normalized = text.replace(',', '')
        return text_normalized

    doc = nlp(text)
    sents = list(doc.sents)
    count_ents = 0
    count_sents = 0

    for sent in sents:
        count_sents += 1
        doc_sent = nlp(sent.text)
        for ent in doc_sent.ents:
            if ent.label_ == 'PER':
                count_ents += 1
        if sent.text.count(',') == 1 and count_ents >= 1:
            text_normalized = text.replace(',', '')
            return text_normalized
        count_ents = 0

    return text_normalized


# convierte el texto en html donde cada tag corresponde a una entidad
# sea profesional, carrera, sede e institucion
def texto_to_html(text, nlp):
    # nlp = spacy.load('es_core_news_md')
    doc = nlp(text)

    colors = {"PER": "linear-gradient(90deg,#FFFF00,#00FFFF)"}
    options = {"colors": colors, "ents": ["PER"]}
    html = displacy.render(doc, style="ent", minify=True, options=options)
    return html


def search_pattern(text):
    regex = r"[;]+([\s][A-Ñ-Z][a-ñ-z]*)*[,]([\s][A-Ñ-Z][a-ñ-z]*)*[;]"

    count = 0

    matches = re.finditer(regex, text, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        count += 1

    if count <= 0:
        return False
    else:
        return True


def test():
    articles = get_articles()
    nlp = spacy.load('es_core_news_md')

    for article in articles:
        print(article[0])
        update_html_article(str(article[0]), texto_to_html(article[2], nlp))


if __name__ == '__main__':
    test()
