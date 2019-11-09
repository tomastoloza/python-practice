import string

# Lista de Stop Words en español
# http://snowball.tartarus.org/algorithms/spanish/stop.txt
_STOP_WORDS = frozenset(['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los',
                         'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'es',
                         'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí',
                         'porque', 'esta', 'son', 'entre', 'está', 'cuando', 'muy', 'sin', 'sobre',
                         'ser', 'tiene', 'también', 'me', 'hasta', 'hay', 'donde', 'han', 'quien',
                         'están', 'estado', 'desde', 'todo', 'nos', 'durante', 'estados', 'todos',
                         'uno', 'les', 'ni', 'contra', 'otros', 'fueron', 'ese', 'eso', 'había',
                         'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo',
                         'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes',
                         'nada', 'muchos', 'cual', 'sea', 'poco', 'ella', 'estar', 'haber', 'estas',
                         'estaba', 'estamos', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te',
                         'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío',
                         'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya',
                         'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro',
                         'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está',
                         'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén',
                         'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría',
                         'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas',
                         'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo',
                         'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras',
                         'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses',
                         'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada',
                         'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han',
                         'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá',
                         'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais',
                         'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube',
                         'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras',
                         'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos',
                         'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas',
                         'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis',
                         'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería',
                         'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais',
                         'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera',
                         'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos',
                         'fueseis', 'fuesen', 'siendo', 'sido', 'sed', 'tengo', 'tienes', 'tiene',
                         'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis',
                         'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán',
                         'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía',
                         'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo',
                         'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos',
                         'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis',
                         'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened', ''])


def acondicionar_palabra(pal):
    reemplazos = (("á", "a"), ("é", "e"), ("ó", "o"), ("ú", "u"))
    pal = pal.lower()
    pal = pal.strip()
    pal = pal.strip(string.punctuation + "»" + "\x97" + "¿" + "¡")
    for a, b in reemplazos:
        pal = pal.replace(a, b)
    return pal


def ii_agregar_archivo(dicc, archivo):
    '''Agrega las palabras del archivo al indice invertido dicc
    archivo es el path completo al archivo, el archivo tiene extensión .txt
    '''
    documento = archivo[:-4]  # elimina la extensión .txt
    with open(archivo, encoding="utf-8", mode="r") as texto:
        for linea in texto:
            for palabra in linea.split():
                palabra = acondicionar_palabra(palabra)
                if palabra not in _STOP_WORDS and len(palabra) > 3:
                    dicc.setdefault(palabra, set())
                    dicc[palabra].add(documento)


def ii_crear(archivos):
    '''Recibe una lista con archivos (path completos) a procesar
    y devuelve un diccionario con el índice invertido
    '''
    dicc = {}
    for archivo in archivos:
        try:
            ii_agregar_archivo(dicc, archivo)
        except IOError as e:
            print(e)
    return dicc


archivos = ["resources/Introduccion.txt", "resources/Bombadil.txt", "resources/Egidio.txt", "resources/Niggle.txt", "resources/Roverandom.txt", "resources/Wootton.txt"]
ii = ii_crear(archivos)
print(ii.keys())
