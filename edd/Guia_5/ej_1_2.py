documentos = {"doc1": "La casa esta ordenada y organizada", \
              "doc2": "Maria se casa el dia de mañana", \
              "doc3": "Maria es muy ordenada y Marta muy organizada", \
              "doc4": "mañana sera un gran dia para visitar a Maria y a Marcela y dejar todo ordenado"}


def indice_invertido(docs):
    '''Recibe un diccionario con documentos, donde la clave es el 
    nombre del documento y el valor el contenido y crea un índice 
    invertido. Devuelve un diccionario, donde las claves son las 
    palabras de los textos y los valores son conjuntos de documentos
    que contienen esas palabras
    '''
    indice = {}
    for doc in docs:
        texto = docs[doc].split()
        for palabra in texto:
            palabra = palabra.lower()
            indice.setdefault(palabra, set())
            indice[palabra].add(doc)
    return indice


dicc = indice_invertido(documentos)
# ejercicio 2

# 1
print("{: <50} {:}".format("1: dia and mañana:", dicc["dia"] & dicc["mañana"]))
# 2
print("{: <50} {:}".format("2: (maría or dia) and not (ordenada):", \
                           {x for x in (dicc["maria"] | dicc["dia"]) if x not in dicc["ordenada"]}))
# 3
print("{: <50} {:}".format("3: (casa and not maría) or (mañana and not maria):", \
                           {x for x in dicc["casa"] if x not in dicc["maria"]} | {x for x in dicc["mañana"] if
                                                                                  x not in dicc["maria"]}))
# 4
print("{: <50} {:}".format("4: (casa or mañana) and not maria:", \
                           {x for x in (dicc["casa"] | dicc["mañana"]) if x not in dicc["maria"]}))
