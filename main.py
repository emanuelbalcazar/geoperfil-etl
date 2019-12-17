import spacy
from src.process.check_utility import is_useful
from src.models.article import get_articles, update_html_article
from src.process.normalize_article import texto_to_html


# def start():
#     articles = get_articles()
#     articles_useful = []
#     count = 0
#
#     for article in articles:
#         if is_useful(article):
#             print(article[0])
#             articles_useful.append(article)
#
#     return articles_useful


def test():
    articles = get_articles()
    print(len(articles))
    nlp = spacy.load('es_core_news_md')

    for article in articles:
        print(article[0])
        update_html_article(article[0], texto_to_html(article[2], nlp))


test()
