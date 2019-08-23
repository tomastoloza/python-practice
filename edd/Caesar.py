import string


class Caesar(object):
    def cifrar(self, frase, clave):
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

    def descifrar(self, frase_cifrada, clave):
        return self.cifrar(frase_cifrada, clave * -1)
