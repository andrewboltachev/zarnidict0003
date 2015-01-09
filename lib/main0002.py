from lib.ex0003 import parse_articles
from lib.ex0002 import f
import json
import fileinput
import pprint
import re

text = []


for line in fileinput.input():
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
    return [x for x in re.split(r'(\[\w+\]|\[\/\w+\]|[\n]|[^\[]+)', line) if x.strip()]


for article in list(articles.items())[20:30]:
    body = article[1]
    line = '\n'.join(body)
    tokens = line_to_tokens(line)
    parsed = f(tokens)
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
