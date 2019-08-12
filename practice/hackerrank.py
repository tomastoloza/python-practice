import re
import textwrap

from jinja2._identifier import pattern


def staircase(n):
    for j in range(1, n + 1):
        print((' ' * (n - j)) + '#' * j)


def miniMaxSum(arr):
    max, min = None, None
    for i in range(arr.__len__()):
        piv = arr.copy()
        piv.remove(arr[i])
        if max is None:
            max = sum(piv)
        if min is None:
            min = sum(piv)
        if sum(piv) > max:
            max = sum(piv)
        elif sum(piv) < min:
            min = sum(piv)
    print(min, max)


def birthdayCakeCandles(ar):
    maximum = max(ar)
    candles = 0
    for i in ar:
        if i == maximum:
            candles += 1
    print(candles)


def countApplesAndOranges(s, t, a, b, apples, oranges):
    quantity_apples, quantity_oranges = 0, 0
    for apple in apples:
        if s <= apple + a <= t:
            quantity_apples += 1
    for orange in oranges:
        if s <= orange + a <= t:
            quantity_oranges += 1
    print(quantity_apples)
    print(quantity_oranges)


def timeConversion(s):
    if s.endswith("AM"):
        if s.startswith("12"):
            return "00" + s[2: s.__len__() - 2]
        else:
            return s[0: s.__len__() - 2]
    else:
        if s.startswith("12"):
            return s[: s.__len__() - 2]
        else:
            return str(int(s[0:2]) + 12) + s[2: s.__len__() - 2]


def wrap(string, max_width):
    print(textwrap.fill(string, max_width))


def parse_html(string):
    separated = string.split(">")
    parsed = re.match(":?(<\w+>)", string)
    print(separated)


if __name__ == '__main__':
    parse_html(
        "<html><head><title>HTML Parser - I</title></head><body data-modal-target class='1'><h1>HackerRank</h1><br "
        "/></body></html>")
