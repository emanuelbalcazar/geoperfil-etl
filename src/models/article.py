import psycopg2
import logging
from src.config.database import config


def get_articles():
    articles = None
    logging.basicConfig(format='%(asctime)s - %(message)s')

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""SELECT id, title, text FROM articles""")
        articles = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        if conn is not None:
            conn.close()
            logging.info("Database connection close.")

    return articles