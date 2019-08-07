from urllib.request import urlopen
from bs4 import BeautifulSoup


def read_html(site):
    html = urlopen(site)
    h1_items = BeautifulSoup(html.read(), features="html.parser").find_all("a")

    for n in h1_items:
        print(str(n).split("href=")[1])


read_html("http://untref.edu.ar")
