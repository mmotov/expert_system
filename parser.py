import re
from rpn import ReversPolishNotation


class Parser:

    def __init__(self):
        self.rpn = ReversPolishNotation()
        self.leftLine = ''
        self.rightLine = ''

    @staticmethod
    def clearString(line):
        line = line.split('#', 1)[0]
        return "".join(line.split())

    def parseLine(self, line):
        line = self.clearString(line)
        self.divideOnLeftAndRight(line)
        self.rpn.toRpn(self.leftLine)
        # print(line)

    def divideOnLeftAndRight(self, line):
        if re.search('=>', line):
            divided = line.split('=>')
            self.leftLine = divided[0]
            self.rightLine = divided[1]
