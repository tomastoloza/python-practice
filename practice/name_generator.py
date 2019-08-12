import json
import random
import string
from time import sleep

if __name__ == '__main__':
    domains = ["@yahoo.com", "@gmail.com", "@hotmail.com"]
    names = open("../resources/names.txt").read()
    for name in names.split("\n"):
        name = name.replace(" ", "").lower() + str(random.randint(2, 2)) + domains[random.randint(0, len(domains)-1)]
        print(name)
        sleep(1)
