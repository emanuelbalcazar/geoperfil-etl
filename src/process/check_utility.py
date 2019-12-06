from src.models.career import get_careers
import spacy
from spacy import displacy

nlp = spacy.load('es_core_news_md')

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    return s

# comprueba si el articulo es de utilidad basandose en diferentes metodos.
# TODO hacer que compruebe usando todos los metodos mas abajo
def is_useful(article):
    if check_title(article[1]) and has_people(article[2]):
        return True
    else:
        return False

# Funciones de comprobación de entidades:

# comprueba si el titulo del articulo contiene ciertas palabras.
def check_title(title):
    keywords = ['matricula', 'colacion', 'titulo', 'titulos', 'graduados', 'egresados', 'egresaron', 'graduaron', 'diplomas']
    contain_word = False
    title = normalize(title.lower()) # quitamos los acentos de los titulos

    for word in keywords:
        if (title.find(word)!= -1):
            contain_word = True

    return contain_word

# comprueba si el texto del articulo menciona a varias personas egresadas.
def has_people(text):
    doc = nlp(text)
    count = 0

    for ent in doc.ents:
        if ent.label_ == "PER":
            count+=1

    return (count > 1)

# comprueba si el texto del articulo menciona una o mas carreras
# TODO pulir
def check_careers(text=str):
    careers = get_careers()
    contain_career = False
    text = normalize(text.lower())

    for career in careers:
        careerNorm = normalize(career[1]).lower()

        if text.find(careerNorm) != -1:
            contain_career = True

    return contain_career