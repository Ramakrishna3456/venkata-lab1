
from Displays import * 


class colorMatchGame:
    def __init__(self):
        print('initial constructor')
        self._mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)

    def testDisplay(self):
        self._mydisplay.showText("hello") 

    def start_game(self, name):
        print("game starts,", name)
        

    def end_game(self):
        print('game ends')

    def pause_game(self):
        print('pause game')

    def resume_game(self):
        print('game resumes') 


class Player(colorMatchGame):
    def __init__(self):

    def resume_game(self):

    def start(self):

    def stop(self):

    def operation(self):

        