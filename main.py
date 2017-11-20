from dialogs import *
from filters import mainMenuFilter

def startMenu():
    print(MSG_START)
    print(MSG_HELP)
    mainMenu()

def mainMenu():
    cmd_q = input(MSG_INPUT)

    while cmd_q not in CMD_LIST:
        print(MSG_INPUT_ERROR)
        cmd_q = input(MSG_INPUT)
        cmd_p = mainMenuFilter(cmd_q)



if __name__ == '__main__':
    startMenu()
