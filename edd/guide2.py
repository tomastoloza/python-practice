import string


def cifrar(frase, clave):
    cypher = ""
    abc = string.ascii_lowercase
    for letter in frase:
        if letter is not " ":
            if (abc.find(letter) + clave) > len(abc) - 1:
                cypher += abc[abc.find(letter) + clave - len(abc)]
            else:
                cypher += abc[abc.find(letter) + clave]
        else:
            cypher += " "
    return cypher


def descifrar(frase_cifrada, clave):
    cypher = ""
    abc = string.ascii_lowercase[::-1]
    for letter in frase_cifrada:
        if letter is not " ":
            if (abc.find(letter) + clave) > len(abc) - 1:
                cypher += abc[abc.find(letter) + clave - len(abc)]
            else:
                cypher += abc[abc.find(letter) + clave]
        else:
            cypher += " "
    return cypher


decy = cifrar("el edulcorante es rico", 7)
print(decy)
print(descifrar(decy, 7))
