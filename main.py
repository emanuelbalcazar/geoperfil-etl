from src.models.article import get_articles
from src.process.check_utility import is_useful


def start():
    articles = get_articles()
    articles_useful = []
    count = 0

    for article in articles:
        if is_useful(article):
            articles_useful.append(article)

    return articles_useful
