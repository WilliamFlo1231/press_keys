from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

keyboard.press('w')
keyboard.press('d')
alternator = True
while True:
    if alternator:
        print('up')
        keyboard.press(Key.ctrl_l)
        time.sleep(2)
        keyboard.release(Key.ctrl_l)
    else:
        print('down')
        keyboard.press(Key.shift_l)        
        time.sleep(5)
        keyboard.release(Key.shift_l)    
    alternator = not alternator