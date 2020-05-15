# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def find_repeated():
    usr_input = input()
    try:
        re_search = re.search(r'([A-Za-z0-9])\1', usr_input)
        print(re_search.group(1))
    except:
        print(-1)


def find_vowels():
    usr_input = input()
    consonants = 'QWRTYPSDFGHJKLZXCVBNM'
    vowels = 'AEIOU'
    try:
        re_search = re.finditer('[QWRTYPSDFGHJKLZXCVBNM]([AEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNM]', usr_input,
                                re.IGNORECASE)
        for x in re_search:
            print(x)
    except:
        print(-1)


def is_valid_alien_user(string):
    regex = r'[_.][0-9]+[A-Za-z]*\_?\b'
    return 'VALID' if re.match(regex, string) else 'INVALID'


def parse_input(function):
    q = input()
    result = []
    for i in range(int(q)):
        r = function(input())
        if r is not None:
            result.append(r)
    print(len(result))


def get_html_link_title(string):
    regex = r'<a href=\"([A-Za-z\/:_.?&=0-9;]+)\".*>(.+)<\/a>'
    search = re.search(regex, string)
    try:
        return search.group(1) + ',' + search.group(2)
    except:
        pass


def is_phone_number(string):
    regex = r'[789]\d{9}'
    boolean = "YES" if re.fullmatch(regex, string) else "NO"
    print(boolean)


def is_UID(string):
    """It must contain at least 2 uppercase English alphabet characters.
    It must contain at least 3 digits ( - ).
    It should only contain alphanumeric characters ( - ,  -  &  - ).
    No character should repeat.
    There must be exactly  characters in a valid UID."""
    re0 = r'[A-Z]{2}'
    re1 = r'\d{3}'
    re2 = r'[A-Za-z0-9]{10}'
    regex_list = [re0, re1, re2]
    result = all(re.match(regex, string) for regex in regex_list)
    return result


# parse_input(get_html_link_title)

# b = get_html_link_title('<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us">Donate to Wikipedia</a></li>')
# b = parse_input(is_phone_number)


def hackerrank_tag():
    q = input()
    result = []
    regex = r'[#@]?hackerrank'
    for i in range(int(q)):
        search = re.search(regex, input(), flags=re.IGNORECASE)
        if search is not None:
            result.append(search)
    return len(result)


# b = parse_input(is_UID)
# b = hackerrank_tag()

def replace_comma(fp):
    with open(fp, 'r') as file:
        read = file.read()
        sub = re.sub('(LICENCIATURA)( EN)', lambda x: x.group(1)[:3] + x.group(2), read)
        print(sub)


def replace_pronouns(string):
    regex = r'(\bel\b|\bla\b|\blas\b|\blos\b)'
    return re.sub(regex,  lambda x: x.group(1)+"!", string)


# b = replace_comma('../resources/materias.txt')
b = replace_pronouns('Decia el cantor: traigo losas, delfines alas y calas para la niña')
print(b)
