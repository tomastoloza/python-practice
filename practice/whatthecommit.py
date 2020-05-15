import os

import requests
from lxml import html
import time


def save_random_commits(quantity):
    with open('what the commits?.txt', 'w+') as file:
        try:
            result = ''
            for n in range(quantity):
                commit = requests.get('http://whatthecommit.com/')
                item = html.fromstring(commit.content)
                print(commit.status_code)
                result += item[1][0][0].text + '\n'
            file.write(result)
        except KeyboardInterrupt:
            file.write(result)


b = os.system('git status')
print(dir(b))
