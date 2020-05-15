import csv

# Ejercicio 1: ¿Cuál es la empresa que más proyectos ejecutó?
import functools
import re


def guia4_ejercicio1():
    with open("edd/Guia 4/1 - empresas-ejecutoras-proyectos.csv", encoding='utf-8', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        empresas = {}

        for line in reader:
            empresas.setdefault(line[1], [])
            empresas[line[1]].append(line[0])

        max = ("", 0)
        for x in empresas:
            max = (x, len(empresas[x])) if len(empresas[x]) > max[1] else max

        print(max[0])


# Ejercicio 2: ¿En cuál provincia se ejecutaron más proyectos de empresas? y ¿Cuál provincia tiene más empresas que ejecutan proyectos?\
def guia4_ejercicio2():
    with open("edd/Guia 4/1 - empresas-ejecutoras-proyectos.csv", encoding='utf-8', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        empresas = {}

        for line in reader:
            empresas.setdefault(line[5], [])
            empresas[line[5]].append(line[0])

        max = ("", 0)
        for x in empresas:
            max = (x, len(empresas[x])) if len(empresas[x]) > max[1] else max

        print('provincia con mas proyectos:\t' + max[0])

        for line in reader:
            empresas.setdefault(line[5], [])
            empresas[line[5]].append(line[1])
        max = ("", 0)
        for x in empresas:
            max = (x, len(empresas[x])) if len(empresas[x]) > max[1] else max
        print('provincia con mas empresas que ejecutan proyectos:\t' + max[0])


# Guia 5

documentos = {"doc1": "La casa esta ordenada y organizada", "doc2": "Maria se casa el dia de mañana",
              "doc3": "Maria es muy ordenada y Marta muy organizada",
              "doc4": "mañana sera un gran dia para visitar a Maria y a Marcela y dejar todo ordenado"}


def indice_invertido(docs):
    '''Recibe un diccionario con documentos, donde la clave es el nombre del documento y el valor el contenido y crea un índice invertido. Devuelve un diccionario, donde las claves son las palabras de los textos y los valores son conjuntos de documentos que contienen esas palabras
    '''
    ind_inv = {}
    for doc in docs:
        for word in docs[doc].split():
            ind_inv.setdefault(word, set())
            ind_inv[word].add(doc)
    print(ind_inv)
    return ind_inv


import string

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
    if pal not in _STOP_WORDS:
        for a, b in (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u')):
            pal = pal.replace(a, b)
        pal = pal.strip()
        pal = pal.strip(string.punctuation)
        pal = pal.lower()
        return pal


def ii_agregar_archivo(dicc, archivo):
    '''Agrega las palabras del archivo al indice invertido dicc
    archivo es el path completo al archivo, el archivo tiene extensión .txt
     '''
    with open(archivo, 'r', encoding='utf-8') as file:
        for word in file.read().split():
            if len(word) > 3:
                word = acondicionar_palabra(word)
                dicc.setdefault(word, set())
                dicc[word].add(archivo)
    return dicc


def ii_crear(archivos):
    dicc = {}
    for archivo in archivos:
        archivo = 'edd/Guia_5/resources/' + archivo
        ii_agregar_archivo(dicc, archivo)
    return dicc


# archivos = ["Introduccion.txt", "Bombadil.txt", "Egidio.txt", "Niggle.txt", "Roverandom.txt", "Wootton.txt"]
# ii = ii_crear(archivos)


def consultar(indice_invertido):
    '''Realiza consultas al indice_invertido, en caso de consultar por una única palabra devuelve los documentos en los que aparece, y en en caso de consultar por varias palabras
    (separadas por blancos) busca alguna de las palabras (OR) y todas las palabras (AND) '''
    while True:
        op = input("\nIntroduce tu búsqueda(Enter para finalizar):\n>>> ")
        if len(op) == 0: break
        busq = op.split()
        if len(busq) == 1:  # op es una sola palabra
            print('\nDocumentos en donde aparece al menos una palabra buscada:' + str(indice_invertido[busq[0]]) + '\n')
        elif len(busq) > 1:
            result = [indice_invertido[acondicionar_palabra(word)] for word in busq]
            or_result = functools.reduce(lambda x, y: x | y, result)
            and_result = functools.reduce(lambda x, y: x & y, result)
            print("\nDocumentos en donde aparece al menos una palabra buscada (OR):" + str(or_result) + "\n")
            print("\nDocumentos en donde aparece al menos una palabra buscada (AND):" + str(and_result) + "\n")


# consultar(ii)


def replace():
    length = input()
    res = ''

    for n in range(int(length)):
        inp = input()
        while re.match(r' \|\| ', inp) is not None or re.match(r' && ', inp) is not None:
            inp = re.sub(r' \|\| ', ' or ', inp)
            inp = re.sub(r' && ', ' and ', inp)
            res += inp + '\n'
    print(res)


clientes = {"Ana": "Valentín Gómez 4733", "Juan": "Caseros 3033"}


def direcciones_pizzeria(clientes):
    with open('resources/direcciones.csv', 'r') as file:
        with open('clientes_con_direccion.csv', 'w+') as file_w:
            reader = csv.reader(file)
            writer = csv.writer(file_w)
            writer.writerow(next(reader))
            for line in reader:
                try:
                    line.append(clientes[line[0]])
                except KeyError:
                    line.append('Direccion desconocida')
                writer.writerow(line)


# direcciones_pizzeria(clientes)

carreras = {"música": ["historia", "piano 1", "piano 2", "guitarra", "composición"],
            "pintura": ["historia", "dibujo 1", "dibujo 2", "pintura 1", "pintura 2"]}

alumnos = {1000: ("Ana", ["música", "pintura"], {"historia": [2, 10], "piano 1": [8], "piano 2": [2]}),
           2000: ("Juan", ["pintura"], {"historia": [6], "dibujo 1": [8], "pintura 1": [2, 7], "dibujo 2": [2]})}


def falta_dar(carreras, alumnos, legajo, carrera):
    try:
        if carrera in alumnos[legajo][1]:
            materias_aprobadas = [materia for materia in alumnos[legajo][2] if
                                  alumnos[legajo][2][materia][len(alumnos[legajo][2][materia]) - 1] > 3]
            print([materia for materia in carreras[carrera] if materia not in materias_aprobadas])
    except KeyError:
        print('Legajo not found')


# falta_dar(carreras, alumnos, 1000, 'música')
# falta_dar(carreras, alumnos, 10200, 'música')

def get_libros_per_codigo(libros):
    with open('resources/docentes_libros.csv', 'r') as file:
        with open('resources/docentes_libros_completo.csv', 'w+') as filew:
            reader = csv.reader(file)
            writer = csv.writer(filew)
            writer.writerow(next(reader))
            for line in reader:
                try:
                    line.append(libros[line[2]][0])
                    line.append(libros[line[2]][1])
                except KeyError:
                    line.append('Libro desconocido')
                    line.append('Autor desconocido')
                writer.writerow(line)


# libros = {"20": ("Mining the Social Web", "M. A. Russell"),
#           "5": ("Data structures and problem solving using Java", "M. A. Weiss")}
# get_libros_per_codigo(libros)

libros = {("Mining the Social Web", "M. A. Russell"): "20",
          ("Data structures and problem solving using Java", "M. A. Weiss"): "5"}

libros_en_uso = {"Estructura de datos": [("Mining the Social Web", "M. A. Russell"), ("Learning Python", "M. Lutz")],
                 "Algoritmos 1": [("Object-Oriented Software Construction", "B. Meyer")],
                 "Algoritmos 2": [("Data structures and problem solving using Java", "M. A. Weiss"),
                                  ("Object-Oriented Software Construction", "B. Meyer")]}


def get_libros_per_materia(libros, libros_en_uso):
    libros_per_materia = {}
    for materia in libros_en_uso:
        for libro in libros_en_uso[materia]:
            if libro not in libros:
                libros_per_materia.setdefault(libro, [])
                libros_per_materia[libro].append(materia)
    print(libros_per_materia)


# get_libros_per_materia(libros, libros_en_uso)


def get_vacantes_map():
    with open('resources/vacantes.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        vacantes = []
        for line in reader:
            vacantes.append((line[1], int(line[2])))
        return vacantes


def get_vacantes_reduce(vacantes):
    print(vacantes)
    dict_vacantes = {}
    for vacante in vacantes:
        dict_vacantes.setdefault(vacante[0], 0)
        dict_vacantes[vacante[0]] += vacante[1]
    return dict_vacantes


# map = get_vacantes_map()
# reduce = get_vacantes_reduce(map)
# print(reduce)


text = 'Hola @Jose25, como estas? Ganamos 2 medallas!'


def get_qletters_map(text):
    text = re.findall(r'\w+', text)
    return [len(word) for word in text]


def get_qletters_reduce(q):
    result = {}
    for item in q:
        result.setdefault(item, 0)
        result[item] += 1
    return result


map = get_qletters_map(text)
izi = get_qletters_reduce(map)
print(izi)
