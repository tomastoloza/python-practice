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
    pass


if __name__ == '__main__':
    countApplesAndOranges(7, 11,
                          5, 15,
                          [-2, 2, 1],
                          [5, -6])
