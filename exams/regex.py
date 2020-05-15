import re


def todos_los_pares(string):
    return [x[0] for x in re.findall(r'(([A-z])\2)', string)]


# reg = todos_los_pares('holaass Juaaaana')
# print(reg)

def get_pronombres(string):
    return [match for match in re.findall(r'la\b|el\b|las\b|los\b', string)]


def get_len_pron(match_list):
    return len(match_list)


# match = get_pronombres('la casa estaba a las dos el uno elefante los los')
# print(match)
# print(get_len_pron(match))

def menos_uno(string):
    regex = r'(\d) (\w+) \1'
    result = re.sub(regex, ree, string)
    print(result)


def ree(match):
    return str(int(match.group(1)) - 1) + ' ' + (match.group(2)) + ' ' + str(int(match.group(1)))


menos_uno('50: 5 casas 5, 3 vasos 3, 1 perro 1')
