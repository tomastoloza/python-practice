import functools
import os
import re
import string
from nltk.stem import SnowballStemmer, LancasterStemmer
from unidecode import unidecode

stemmer = SnowballStemmer('spanish')


def create_inverted_index(files):
    index = {}
    for file_name in files:
        with open("resources/" + file_name, 'r') as file:
            file = file.read()
            for word in file.split():
                word = acondicionar_palabra(word)
                if word is not None and word not in _STOP_WORDS and len(word) > 3:
                    index.setdefault(word, set())
                    index[word].add(file_name)
    return index


_STOP_WORDS = frozenset(['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los',
                         'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'es', 'lo', 'como',
                         'más', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 'esta', 'son',
                         'entre', 'está', 'cuando', 'muy', 'sin', 'sobre', 'ser', 'tiene', 'también', 'me', 'hasta',
                         'hay', 'donde', 'han', 'quien', 'están', 'estado', 'desde', 'todo', 'nos', 'durante',
                         'estados', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'fueron', 'ese', 'eso', 'había',
                         'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras',
                         'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'sea',
                         'poco', 'ella', 'estar', 'haber', 'estas', 'estaba', 'estamos', 'algunas', 'algo', 'nosotros',
                         'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os',
                         'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos',
                         'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros',
                         'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está', 'estamos', 'estáis', 'están',
                         'esté', 'estés', 'estemos', 'estéis', 'estén', 'estaré', 'estarás', 'estará',
                         'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais',
                         'estarían', 'estaba', 'estabas', 'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste',
                         'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos',
                         'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis',
                         'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha',
                         'hemos', 'habéis', 'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás',
                         'habrá', 'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais',
                         'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo',
                         'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais',
                         'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo',
                         'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea',
                         'seas', 'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán',
                         'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais',
                         'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fuéramos',
                         'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'siendo', 'sido',
                         'sed', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas',
                         'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis',
                         'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía',
                         'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos',
                         'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran',
                         'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida',
                         'tenidos', 'tenidas', 'tened', ''])


def acondicionar_palabra(pal):
    if not re.compile(r'\w+=.+').match(pal) and not re.compile(r'<[^>]+>').match(pal) \
            and not re.compile(r'\d+').search(pal):
        if pal not in _STOP_WORDS and len(pal) > 3:
            pal = unidecode(pal)
            pal = pal.lower()
            pal = pal.strip(string.punctuation)
            pal = stemmer.stem(pal)
            return pal


def consultar(indice_invertido):
    '''Realiza consultas al indice_invertido, en caso de consultar por una única palabra devuelve los documentos en los que aparece, y en en caso de consultar por varias palab
    ras
    (separadas por blancos) busca alguna de las palabras (OR) y todas las palabras (AND) '''
    while True:
        op = input("\nIntroduce tu búsqueda(Enter para finalizar):\n>>> ")
        try:
            if len(op) == 0:
                break
            busq = op.split()
            if len(busq) == 1:  # op es una sola palabra
                print(indice_invertido[acondicionar_palabra(busq[0])])
            elif len(busq) > 1:
                result = [indice_invertido[acondicionar_palabra(word)] for word in busq]
                print(result)
                or_result = functools.reduce(lambda x, y: x | y, result)
                and_result = functools.reduce(lambda x, y: x & y, result)
                print("\nDocumentos en donde aparece al menos una palabra buscada (OR)\n")
                print(or_result)
                print("\nDocumentos en donde aparecen todas las palabras buscadas (AND)\n")
                print(and_result)
        except KeyError:
            print(op + ' not found')


def searcher(words, inverted_index):
    result = []
    for word in words.split():
        try:
            docs = functools.reduce(lambda x, y: x + ", " + y,
                                    [doc for doc in inverted_index[acondicionar_palabra(word)]])
            result.append((word, docs))
        except KeyError:
            result.append((word, {}))
        except TypeError:
            pass
    return result


def search(inverted_index):
    while True:
        user_input = input("\nIntroduce tu búsqueda (Enter para finalizar):\n>>> ")
        if len(user_input) == 0:
            break
        results = searcher(user_input, inverted_index)
        for result in results:
            if len(result[1]) > 0:
                print('La palabra ' + result[0] + ' apareció en los documentos: ' + result[1])
            else:
                print('La palabra ' + result[0] + ' no tuvo apariciones')


if __name__ == '__main__':
    file = {"doc1": "La casa esta ordenada y organizada", \
            "doc2": "Maria se casa el dia de mañana", \
            "doc3": "Maria es muy ordenada y Marta muy organizada", \
            "doc4": "mañana sera un gran dia para visitar a Maria y a Marcela y dejar todo ordenado"}
    b = create_inverted_index(["Bombadil.txt",
                               "Egidio.txt",
                               "Introduccion.txt",
                               "Niggle.txt",
                               "Roverandom.txt",
                               "Wootton.txt"])
    search(b)
