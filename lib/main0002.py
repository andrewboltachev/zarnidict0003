from lib.ex0003 import parse_articles
import json
import fileinput

text = []


for line in fileinput.input():
    line = line.rstrip('\n')
    text.append(line)

for line in text:
    print(line)

#json.dumps(articles)
