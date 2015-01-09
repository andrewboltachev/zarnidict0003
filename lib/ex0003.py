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

    for i, line in enumerate(text.split('\n')):
        if state == LineKind.NOTHING:
            if kind(line) == LineKind.NOTHING:
                pass
            elif kind(line) == LineKind.NAME:
                state = LineKind.NAME
                name = line
            elif kind(line) == LineKind.BODY:
                raise ArticlesParsingError("BODY after NOTHING unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.ENDING:
                raise ArticlesParsingError("ENDING after NOTHING unexpected (line {0})".format(i + 1))

        elif state == LineKind.NAME:
            if kind(line) == LineKind.NOTHING:
                raise ArticlesParsingError("NOTHING after NAME unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.NAME:
                raise ArticlesParsingError("NAME after NAME unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.BODY:
                state = LineKind.BODY
                body = [line]
            elif kind(line) == LineKind.ENDING:
                raise ArticlesParsingError("ENDING after NAME unexpected (line {0})".format(i + 1))

        elif state == LineKind.BODY:
            if kind(line) == LineKind.NOTHING:
                raise ArticlesParsingError("NOTHING after BODY unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.NAME:
                raise ArticlesParsingError("NAME after BODY unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.BODY:
                body.append(line)
            elif kind(line) == LineKind.ENDING:
                state = LineKind.ENDING
                result[name] = body

        elif state == LineKind.ENDING:
            if kind(line) == LineKind.NOTHING:
                state = LineKind.NOTHING
            elif kind(line) == LineKind.NAME:
                state = LineKind.NAME
                name = line
            elif kind(line) == LineKind.BODY:
                raise ArticlesParsingError("BODY after ENDING unexpected (line {0})".format(i + 1))
            elif kind(line) == LineKind.ENDING:
                raise ArticlesParsingError("ENDING after ENDING unexpected (line {0})".format(i + 1))

    return result
