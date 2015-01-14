from lib.ex0003 import parse_articles
from lib.ex0002 import f
import json
import fileinput
import pprint
import re
import sys
import os

text = []

argv = sys.argv[1:]

FILENAME =  argv[0] if len(argv) else os.environ.get('DICT_FILENAME', None)

if FILENAME is None:
    sys.stderr.write('Укажите имя файла в качестве аргумента либо установите переменную среды DICT_FILENAME\n')
    sys.exit(1)

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


def Plus(*args):
    return Seq(
        *(list(args) + [Star(*args)])
    )

Либо = Or
Посл = Seq
НольИлиБольше = Star
ОдинИлиБольше = Plus
МожетБыть = MayBe
Символ = Char


преамбула = Посл(
    МожетБыть(Символ('pre')),
    МожетБыть(Символ('end')),
    МожетБыть(Символ('m1')),
)

пример_без_автора = Seq(
    Символ('mhr'),
    Символ('rus'),
    name='пример без автора',
)

пример_с_автором = Seq(
    Символ('mhr'),
    Символ('aut'),
    Символ('rus'),
    name='пример без автора',
)

пример = Либо(
    пример_с_автором,
    пример_без_автора
)

собственно_ссылка = Посл(
    Символ('ref'),
    МожетБыть(Символ('u')),
)

ссылка = Посл(
    Символ('ex'),
    собственно_ссылка,
    НольИлиБольше(
        Посл(
            Символ('COMMA'),
            собственно_ссылка
        )
    )
)

перевод = Посл(
    преамбула,
    Символ('trn'),
    НольИлиБольше(пример, name='примеры'),
    НольИлиБольше(ссылка)
)

настоящая_статья = Посл(
    ОдинИлиБольше(перевод)
)

статья_состоящая_только_из_преамбулы = Посл(
    преамбула
)

простая_статья = Либо(
    настоящая_статья,
    статья_состоящая_только_из_преамбулы
)

статья_с_римскими_цифрами = Посл(
    преамбула,
    ОдинИлиБольше(
        Посл(
            Символ('R'),
            преамбула,
            простая_статья
        )
    )
)

статья_с_литерами = Посл(
    преамбула,
    ОдинИлиБольше(
        Посл(
            Символ('L'),
            преамбула,
            Либо(
                простая_статья,
                статья_с_римскими_цифрами
            )
        )
    )
)

sm = Либо(
    статья_с_литерами,
    статья_с_римскими_цифрами,
    простая_статья
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
        def p(x, l=level, pl=''):
            if pl:
                pl = '\t' + pl
            print(('  ' * l) + str(x) + pl)
        if 'name' in x:
            pl = ''
            if 'payload' in x:
                pl = str(x['payload']).replace('\n', ' ')

            p(x['name'], l=level, pl=pl)
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
        #jd(parsed2)
    try:
        r = sm.run(iter(parsed4))
    except AutomatonException as e:
        perr(e)
        break
    else:
        print(article[0], 'OK')
        #jd(r.to_json_like())
        sd(r.to_json_like())
        print('')
        print('')
        print('')
