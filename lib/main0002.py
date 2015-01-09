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
    return [x for x in re.split(r'(\[\w+\]|\[\/\w+\]|[^\[]+)', line) if x]


for article in list(articles.items())[20:30]:
    body = article[1]
    for line in body:
        print(line)
        print(line_to_tokens(line))
        print('')
        print('')
        print('')
    #print(f(body))
