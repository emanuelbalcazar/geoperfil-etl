import psycopg2
import logging as log
from src.config.database import config


def get_articles():
    articles = None
    log.basicConfig(format='[%(asctime)s - %(message)s]')

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""SELECT id, title, text , is_processed FROM articles WHERE is_processed IS FALSE""")
        articles = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        log.error(error)
    finally:
        if conn is not None:
            conn.close()
            log.info("Database connection close...")

    return articles


