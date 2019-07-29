def is_palindrome(string):
    if string.__len__() == 1:
        return True
    else:
        return is_palindrome(string[:int(len(string) / 2) - 1])


print(is_palindrome("asda2dsa"))
