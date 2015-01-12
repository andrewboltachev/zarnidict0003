from lib.ex0003 import parse_articles
from lib.ex0002 import f
import json
import fileinput
import pprint
import re
import sys

text = []

argv = sys.argv[1:]

FILENAME = argv[0] if len(argv) else '/home/andrey/docs/zarnidict0001/dicts/chm-rus/marirus.dsl'

with open(FILENAME) as fi:
    for line in fi:
        line = line.rstrip('\n')
        if len(line):
            if line[0] == '#':
                continue
        text.append(line)

#for line in text:
#    print(line)


articles = parse_articles(text)

# do sth with them...

def line_to_tokens(line):
    return [x for x in re.split(r'([\n]|\[\w+\]|\[\/\w+\]|[^\[]+)', line) if x.strip()]

def tr(x):
    if x == '':
        return ''
    elif x == ', ':
        return 'COMMA'
    elif x == 'Г.: ':
        return 'G'
    elif x == 'Г.':
        return 'GG'
    else:
        return x

try:
    unichr
except NameError:
    unichr = chr


from lib.ex0006 import (
    Char, Seq, Or, Star, MayBe,
    InputChar,
    AutomatonException
)

EX = Or(
    Seq(
        Char('mhr'),
        Char('rus'),
        name='пример без автора',
    ),
    Seq(
        Char('mhr'),
        Char('u'),
        Char('rus'),
        name='пример с автором',
    ),
    name='пример',
)

REF = Seq(
    Char('ex'),
    Char('ref'),
    Star(
        Seq(
            Char('COMMA'),
            Char('ref'),
        )
    ),
    name='ссылки',
)

T = Seq(
    Char('trn'),
    Star(EX, name='примеры'),
    name='перевод значения'
)

sm = Seq(
    Seq(
        Char('pre'),
        MayBe(Char('m1'), name='пояснение'),
    ),
    Seq(
        #T,
        Star(T, name='...'),
        name='перевод'
    ),
    MayBe(REF),
    name='статья',
)


one = ord(u'Ⅰ')
roman_numbers = [unichr(x) for x in range(one, one + 12)]

for article in list(articles.items()):
    body = article[1]
    line = '\n'.join(body)
    tokens = line_to_tokens(line)
    parsed = f(tokens)
    parsed3 = [] # FIXME: должно быть разбито по переносам строки заранее при токенизации
    for item in parsed:
        try:
            item['name']
        except TypeError:
            for x in item.split('\n'):
                if x.strip():
                    parsed3.append(x)
        else:
            parsed3.append(item)

    parsed2 = []
    for item in parsed3:
        if item in ['А.', 'Б.']:
            item = {'name': 'L', 'data': item}
        if item in roman_numbers:
            item = {'name': 'R', 'data': item}
        try:
            item['name']
        except TypeError:
            item = {'name': tr(item), 'data': None}
        if item['name'] == 'ex' and item['data'] in map(lambda v: [v], [
                'Идиоматические выражения:',
                'Составные глаголы:',
            ]):
            item = {'name': 'exi', 'data': item['data']}
        if item['name'] == 'i':
            item = {'name': 'exi', 'data': item['data']}
        if item['name'] == 'm1' and item['data'][:1] == ['– ']:
            item = {'name': 'm1dash', 'data': item['data']}
        parsed2.append(item)

    parsed4 = [InputChar(name=x['name'], payload=x['data']) for x in parsed2]
    def sd(x, level=0):
        def p(x, l=level):
            print(('  ' * l) + str(x))
        if 'name' in x:
            p(x['name'])
            if 'content' in x:
                if isinstance(x['content'], list):
                    for y in x['content']:
                        sd(y, level + 1)
                else:
                    sd(x['content'], level + 1)
        else:
            p(x)
    def jd(x):
        print(json.dumps(x, indent=4, ensure_ascii=False))
    def perr(e='FAIL'):
        print(article[0], e)
        print('')
        jd(parsed2)
    try:
        r = sm.run(iter(parsed4))
    except AutomatonException as e:
        perr(e)
        break
    else:
        print(article[0], 'OK')
        sd(r.to_json_like())
        print('')
        print('')
        print('')
