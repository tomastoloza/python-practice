import csv
import random
import math


def isPalindrome(string):
    string = string.replace(" ", "")
    return string == string[::-1]


def isPrimeNumber(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def sumAndAvg(list):
    sum = 0
    for n in list:
        sum += n
    return sum / len(list)


def getFactorial(num):
    if num == 0:
        return 1
    else:
        for i in range(1, num):
            num = num * i
        return num


def getPosNegEqual(list, n):
    pos, neg, equal = [], [], []
    for i in list:
        if i > n:
            pos.append(i)
        if i == n:
            equal.append(i)
        if i < n:
            neg.append(i)
    return [pos, neg, equal]


def getQuantityOfLetters(string):
    dic = {}
    for i in string:
        dic[i] = string.count(i)
    return dic


def findNotRepeated(l1, l2):
    return l1 ^ l2


def tabla_de_posiciones(puntajes):
    results = {}
    for group1, score1, group2, score2 in puntajes:
        results.setdefault(group1, 0)
        results.setdefault(group2, 0)
        if score1 > score2:
            results[group1] += 3
        elif score1 < score2:
            results[group2] += 3
        else:
            results[group1] += 1
            results[group2] += 1
    return results


def get_grades_from_csv(file_alumnos, file_notas):
    alumnos = csv.reader(open(file_alumnos, "r"), delimiter=",")
    notas = csv.reader(open(file_notas, "r"), delimiter=",")
    dict_alumnos = {}
    next(alumnos)
    for padron, apellido, nombre, carrera in alumnos:
        dict_alumnos.setdefault(padron, {})
        dict_alumnos[padron]['apellido'] = apellido
        dict_alumnos[padron]['nombre'] = nombre
        dict_alumnos[padron]['carrera'] = carrera
        dict_alumnos[padron].setdefault('materia', [])
    for padron, materia, nota in notas:
        dict_alumnos[padron]['materia'].append((materia, nota))

    for key in dict_alumnos:
        alumno = dict_alumnos[key]
        print("{}, {} - {}".format(alumno['nombre'], alumno['apellido'], key))
        for materia in alumno['materia']:
            print("{}: {}".format(materia[0], materia[1]))


def get_random(file):
    file = open(file, "r")
    names = [name[:-1] for name in file]
    return names[random.randint(0, len(names) - 1)].split(" ")


def generate_random_csv(file):
    """padron apellido nombre carrera"""
    writer = csv.writer(open(file, "w"))
    writer.writerow(["padron", "apellido", "nombre", "carrera"])
    for i in range(10):
        fullname = get_random("../resources/names.txt")
        materia = " ".join(get_random("../resources/materias.txt"))
        writer.writerow([random.randint(0, 999999), fullname[1], fullname[0], materia])


if __name__ == '__main__':
    # generate_random_csv("../resources/alumnos.csv")
    # get_name("../resources/names.txt")
    get_grades_from_csv("../resources/alumnos.csv", "../resources/notas.csv")
