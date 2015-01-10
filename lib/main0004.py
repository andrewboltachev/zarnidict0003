from lib.ex0003 import parse_articles
from lib.ex0002 import f
import json
import fileinput
import pprint
import re
import sys

text = []

with open(sys.argv[1]) as fi:
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

from lib.sm0001 import sm
from lib.ex0004 import StateMachineError


def tr(x):
    if x == '':
        return ''
    elif x == ', ':
        return 'COMMA'
    elif x == 'Г.: ':
        return 'G'
    else:
        return x

try:
    unichr
except NameError:
    unichr = chr

one = ord(u'Ⅰ')
roman_numbers = [unichr(x) for x in range(one, one + 12)]

for article in list(articles.items()):
    body = article[1]
    line = '\n'.join(body)
    tokens = line_to_tokens(line)
    parsed = f(tokens)
    '''
    print(line)
    print(tokens)
    print('')
    print('')
    print('')
    #print(json.dumps(parsed, ensure_ascii=False))
    pprint.pprint(parsed)
    print('')
    print('')
    print('')
    '''
    parsed3 = []
    for item in parsed:
        try:
            item['name']
        except TypeError:
            for x in item.split('\n'):
                parsed3.append(x)
        else:
            parsed3.append(item)

    parsed2 = []
    for item in parsed3:
        if item in roman_numbers:
            item = {'name': 'R', 'data': item}
        try:
            item['name']
        except TypeError:
            item = {'name': tr(item), 'data': None}
        if item == {'name': 'ex', 'data': ['Идиоматические выражения:']}:
            item = {'name': 'exi', 'data': None}
        if item['name'] == 'm1' and item['data'][:1] == ['– ']:
            item = {'name': 'm1dash', 'data': item['data']}
        parsed2.append(item)
    try:
        sm.run(parsed2)
    except StateMachineError as e:
        print(article[0], e)
        print('')
        pprint.pprint(parsed2)
        break
    else:
        print(article[0], 'OK')
