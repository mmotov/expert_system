import os.path
import colors
from parser import Parser


class Controller:

    def __init__(self):
        self.parser = Parser()

    def manageLine(self, line):
        self.parser.parseLine(line)

    def readUserInput(self):
        line = ''
        while not self.endOfInput(line):
            line = input()
            self.manageLine(line)

    def readFile(self, filename):
        if os.path.isfile(filename):
            with open(filename) as f:
                for line in f:
                    self.manageLine(line)
        else:
            print(colors.red('No such file or directory'))

    @staticmethod
    def endOfInput(line):
        if len(line) and line[0] == '?':
            return True
        else:
            return False
