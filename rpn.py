import re
import colors


class ReversPolishNotation:

    operations = ['(', ')', '^', '|', '+']

    def __init__(self):
        self.input = ''
        self.output = []
        self.stack = []

    def toRpn(self, line):
        if line:
            self.input = line
            print(self.input)
            for index, char in enumerate(self.input):
                if char in self.operations:
                    self.manageOperation(char)
                elif re.fullmatch('^[A-Za-z]$', char):
                    self.output.append(char)
            self.moveStackToInput()
            print('===============')
            print('stack: ', self.stack)
            print('output: ', self.output)

        else:
            raise Exception(colors.red('Nothing to convert in revers polish notation'))

    def manageOperation(self, operation):
        if operation is ')':
            print(colors.red('ALERTTT'))
            self.moveStackToInput()
        elif not len(self.stack) or self.stackLessPriority(operation) or operation is '(':
            self.addOperationToStack(operation)
        elif self.stackHigherOrEqualPriority(operation):
            self.moveFirstOperationFromStackToInput()
            self.addOperationToStack(operation)

    def stackLessPriority(self, operation):
        return self.operations.index(self.stack[0]) < self.operations.index(operation)

    def stackHigherOrEqualPriority(self, operation):
        return self.operations.index(self.stack[0]) >= self.operations.index(operation)

    def addOperationToStack(self, operation):
        self.stack.insert(0, operation)

    def moveFirstOperationFromStackToInput(self):
        operation = self.stack.pop(0)
        self.output.append(operation)

    def moveStackToInput(self):
        while self.stack:
            if self.stack[0] is '(':
                del self.stack[0]
                break
            else:
                self.moveFirstOperationFromStackToInput()
