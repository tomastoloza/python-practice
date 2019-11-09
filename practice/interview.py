def isAnagram(s1, s2):
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return "".join(sorted(s1))


def funWithAnagrams(s):
    result = []
    for word in s:
        for word2 in s:
            print(isAnagram(word, word2))


if __name__ == '__main__':
    print(funWithAnagrams(["code",
                           "aaagmnrs",
                           "anagrams",
                           "doce"]))
