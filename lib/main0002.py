from lib.ex0003 import parse_articles
import json
import fileinput
import pprint

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

pprint.pprint(articles)
