from pynput.keyboard import Key, Controller
import time



keyboard = Controller()

def press_key(key):
    # For limiting the frequency of press
    # time.sleep(1)
    ## cheking of keypress is not a charachter then apply special format.
    if len(key) > 1:
        key = getattr(Key,key)
        keyboard.press(key)
        keyboard.release(key)
    ### if it's simple character then there is no issue.
    else:
        keyboard.press(key)
        keyboard.release(key)


def main():
    time.sleep(10)
    for i in range(10):
        press_key('right')



main()
