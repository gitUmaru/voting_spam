import time
import pynput.mouse as pymouse
mouse = pymouse.Controller()
while True:
    mouse.position = (1114, 440)
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(5)
    mouse.press(pymouse.Button.left)
    mouse.release(pymouse.Button.left)
    mouse.position = (80, 50)
    mouse.press(pymouse.Button.left)
    mouse.release(pymouse.Button.left)
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(60)
