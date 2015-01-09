from collections import OrderedDict

class LineKind(object):
    NOTHING = 0
    NAME = 1
    BODY = 2
    ENDING = 3

    @classmethod
    def for_line(self, line):
        if line == '\t':
            return self.ENDING
        if line.strip() == '':
            return self.NOTHING
        else:
            if line[0] == '\t':
                return self.BODY
            else:
                return self.NAME


class ArticlesParsingError(Exception):
    pass


def parse_articles(text):
    result = OrderedDict([])

    state = LineKind.NOTHING

    name = None
    body = []

    kind = LineKind.for_line

    for line in text.split('\n'):
        if state == LineKind.NOTHING:
            if kind(line) == LineKind.NAME:
                name = line
            elif kind(line) == LineKind.BODY:
                pass
            elif kind(line) == LineKind.ENDING:
                pass
            elif kind(line) == LineKind.NOTHING:
                pass
        elif state == LineKind.NAME:
            pass
        elif state == LineKind.BODY:
            pass
        elif state == LineKind.ENDING:
            pass

    return result
