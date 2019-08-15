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


def getPos(string):
    print(string.find("python"))


if __name__ == '__main__':
    math.modf()

