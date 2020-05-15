import os

path = '/Users/ttoloza/Desktop/text/'

if not os.path.exists(path + '/images'):
    os.mkdir(path + '/images')

dir = os.walk(path)

files = []
for x in dir:
    files.append([x[0] + item for item in x[2]])


print(files)