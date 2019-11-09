import functools


# ejercicio 2
def ee():
    falopa = map(lambda x: x if x > 0 else x * -1, [5, -200, -7, 6])
    res = functools.reduce(lambda x, y: x if x > y else y, falopa)
    print(res)


def aa():
    result = {"doc1": "La casa esta ordenada y organizada", \
              "doc2": "Maria se casa el dia de mañana", \
              "doc3": "Maria es muy ordenada y Marta muy organizada", \
              "doc4": "mañana sera un gran dia para visitar a Maria y a Marcela y dejar todo ordenado"}

    result = {'clave 1': {'doc1', 'doc2'}, 'clave 2': {'doc3', 'doc4'}}
    clave1 = {'doc1', 'doc2'}
    clave2 = {'doc3', 'doc4'}

    # a = map(lambda x: x, [clave1, clave2])
    b = functools.reduce(lambda x, y: x | y, [clave1, clave2])
    print([x for x in b])


aa()
