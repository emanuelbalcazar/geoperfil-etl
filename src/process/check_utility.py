from src.models.career import get_careers


def is_useful(article):
    if check_title(article[1]):
        if check_careers(article[2]):
            return True
        else:
            return False


def check_title(title):
    keywords = ['matrícula', 'colación', 'título', 'titulos', 'graduados', 'egresados', 'egresaron', 'graduaron']
    contain_word = False

    for word in keywords:
        print(title.find(word))
        if title.find(word) != -1:
            contain_word = True

    return contain_word


def check_careers(text=str):
    careers = get_careers()
    contain_career = False

    for career in careers:
        if text.find(career[1]) != -1:
            contain_career = True

    return contain_career
