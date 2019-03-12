# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:22:58 2019

@author: umaru
"""

import pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller


mouse = Controller()
keyboard = Controller()

# Set pointer position
mouse.position = (1114, 440)
print('The current pointer position is {0}'.format(
        mouse.position))
mouse.press(Button.left)
mouse.release(Button.left)

keyboard.press(Key.f)
keyboard.release(Key.f)
