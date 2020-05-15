import csv
import functools
import re

str = "Hola @Jose25, como estas? Ganamos 2 medallas!"


def get_words(string):
    return [x for x in re.findall(r'\w+', string)]


def get_quantity(list_string):
    result = {}
    for item in list_string:
        result.setdefault(len(item), 0)
        result[len(item)] += 1
    return result


def get_schools(fp):
    with open(fp, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return [(x[1], int(x[2])) for x in reader]


def get_availability(map_object):
    result = {}
    for item in map_object:
        result.setdefault(item[0], 0)
        result[item[0]] += item[1]
    return result


a = get_schools('escuelas.csv')
a = get_availability(a)
print(a)
