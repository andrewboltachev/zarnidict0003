from lib.ex0003 import parse_articles
from lib.ex0002 import f
import json
import pprint
import re
import sys
import os
from collections import OrderedDict


def get_last():
    try:
        with open('last.txt') as f:
            return f.read().strip()
    except:
        return None

def save_last(x):
        with open('last.txt', 'w') as f:
            f.write(x)

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
    InputChar,
    AutomatonException
)

from .main0007 import sm

one = ord(u'Ⅰ')
roman_numbers = [unichr(x) for x in range(one, one + 12)]


last_last = None #get_last()
last = None
trigger = False


r0 = OrderedDict()

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
        pprint.pprint(parsed2)

    if (last_last is not None) and not trigger:
        print(article[0], 'IGN')
        if article[0] == last_last:
            trigger = True
    else:
        #print(parsed4)
        r0[article[0]] = parsed4
        continue
        try:
            r = sm.run(iter(parsed4))
        except AutomatonException as e:
            perr(e)
            break
        else:
            last = article[0]
            print(article[0], 'OK')
            #jd(r.to_json_like())
            sd(r.to_json_like())
            print('')
            print('')
            print('')


if last is not None:
    save_last(last)


print(json.dumps([[k, [{'type': 'InputChar', 'name': x.name, 'payload': x.payload } for x in v]] for k, v in r0.items()], ensure_ascii=False))
