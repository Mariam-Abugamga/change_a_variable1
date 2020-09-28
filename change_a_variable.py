# Created By: Mariam Abugamga
# Date: sept, 28, 2020
# Program changes a variable 
#

from microbit import *


hungryness = 0

while True:
    if button_a.is_pressed():
        hungryness = hungryness + 1
    elif button_b.is_pressed():
        hungryness = hungryness - 1 
    display.show(hungryness)
    sleep(500)

