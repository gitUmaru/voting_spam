import pynput
import time
import pynput.mouse as pymouse
import pynput.keyboard as pykey

delay = 2.00
start = pykey.KeyCode(char='o')
end = pykey.KeyCode(char='p')

mouse = pymouse.Controller()
keyboard = pykey.Controller()

# Set pointer position
mouse.position = (1114, 440)
print('The current pointer position is {0}'.format(
        mouse.position))
mouse.press(pymouse.Button.left)
mouse.release(pymouse.Button.left)

keyboard.press(pykey.Key.f5)
keyboard.release(pykey.Key.f5)

while True:
    print("I print")
    time.sleep(delay)
