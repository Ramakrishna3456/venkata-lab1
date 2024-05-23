import time
time.sleep(0.1) # Wait for USB to become ready

from colorMatcherGame import *

print("Hello, Pi Pico!")

colormatchgame = colorMatchGame()

# colormatchgame.testDisplay()

colorMatchGame.start_game()



