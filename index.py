import sys
from controller import Controller


controller = Controller()

if len(sys.argv) > 1:
    controller.readFile(sys.argv[1])
else:
    controller.readUserInput()
