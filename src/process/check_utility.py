from src.models.career import get_careers

# comprueba si el articulo es de utilidad basandose en diferentes metodos.
# TODO hacer que compruebe usando todos los metodos mas abajo
def is_useful(article):
    if check_title(article[1]):
        if check_careers(article[2]):
            return True
        else:
            return False

# Funciones de comprobación de entidades:

# comprueba si el titulo del articulo contiene ciertas palabras.
# TODO pulir
def check_title(title):
    keywords = ['matrícula', 'colación', 'título', 'titulos', 'graduados', 'egresados', 'egresaron', 'graduaron']
    contain_word = False

    for word in keywords:
        if title.find(word) != -1:
            contain_word = True

    return contain_word

# comprueba si el texto del articulo menciona una o mas carreras
# TODO pulir
def check_careers(text=str):
    careers = get_careers()
    contain_career = False

    for career in careers:
        if text.find(career[1]) != -1:
            contain_career = True

    return contain_career

# comprueba si el texto del articulo menciona a varias personas egresadas.
# TODO implementar
def has_people(text):
    return True

# comprueba si el texto del articulo menciona alguna sede institucional.
# TODO implementar
def has_campus(text):
    return True

# comprueba si el texto del articulo menciona alguna institucion.
# TODO implementar
def has_institution(text):
    return True