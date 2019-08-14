import re
import textwrap

from jinja2._identifier import pattern

import re
import numpy


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
    j = 0
    while j < len(string) - 1:
        print(string[j:j + max_width])
        j += max_width


def getRunnerUp(arr):
    maximum = max(arr)
    while max(arr) == maximum:
        arr.remove(max(arr))
    print(max(arr))


def detectFloat(string):
    reg = re.compile("((\+|\-)?\d+\.\d+)|(\+|\-)?\.\d+").fullmatch(string)
    if type(reg) == re.Match:
        print(True)
    else:
        print(False)


def splitNumber(string):
    for i in re.split(",|\.", string):
        print(i)


def getFirstOccurrence(string):
    print(re.compile("\w|\d").fullmatch(string))


def getProductOfSum(arr):
    print(numpy.prod(numpy.sum(arr, axis=0)))


def swap_case(s):
    string = ""
    for i in s:
        if i.islower():
            string += i.upper()
        elif i.isupper():
            string += i.lower()
        else:
            string += i
    print(string)


def split_and_join(line):
    return "-".join(line.split(" "))


def count_substring(string, sub_string):
    for i in range(0, len(string)):
        print(string)
    return


def getLowestGrades(students):
    grades = []
    lowest = []
    dicty = {}
    for i in students:
        dicty[i[0]] = i[1]

    print(lowest)


def doMap(a, b, c):
    a[b] = c
    return a


def readAndOperate():
    n = int(input())
    print("\n")
    listy = []
    for it in range(0, n):
        i = input()
        if i.startswith("insert"):
            op = i.split(" ")
            listy.insert(int(op[1]), int(op[2]))
        if i.startswith("print"):
            print(listy)
        if i.startswith("remove"):
            op = i.split(" ")
            listy.remove(int(op[1]))
        if i.startswith("append"):
            op = i.split(" ")
            listy.append(int(op[1]))
        if i.startswith("sort"):
            listy.sort()
        if i.startswith("pop"):
            listy.pop()
        if i.startswith("reverse"):
            listy.reverse()

def getHashTuple():
    n = int(input())
    integer_list = map(int, input().split())
    asd = ()
    asd.__add__("s")
    print(asd)

if __name__ == '__main__':
    getHashTuple()
