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


if __name__ == '__main__':
    print(timeConversion("07:05:45AM"))
    print(timeConversion("12:05:45PM"))
    print(timeConversion("01:05:45PM"))
    print(timeConversion("12:40:22AM"))
