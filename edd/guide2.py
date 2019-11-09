from edd.Caesar import Caesar


def cifrar_archivo(entrada, salida, clave):
    open(salida, "w+").write(Caesar().cifrar(open(entrada, "r").read(), clave))


def decifrar_archivo(entrada, salida, clave):
    open(salida, "w+").write(Caesar().descifrar(open(entrada, "r").read(), clave))


if __name__ == '__main__':
    cifrar_archivo("../resources/cypher_message.txt", "../resources/cripted_message.txt", 3)
    decifrar_archivo("../resources/cripted_message.txt","../resources/decripted_message.txt", 3)
