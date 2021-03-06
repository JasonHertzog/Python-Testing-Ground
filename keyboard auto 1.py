# documentation used: https://github.com/boppreh/keyboard#api
from pynput.keyboard import Key, Controller
import keyboard
# Importing os to be able to clear console and keep it clean when showing script.
import os

# This is used to press enter with pynput
enterboard = Controller() 
# Keep hotkey set to shift, otherwise the script can break.
hotkey = 'shift'

directory = "C:\\Users\\Jhert\\OneDrive\\Documents\\Notepad ++\\Learn Java\\"
file = open(directory + "placeholder", 'r')
f = file.readlines()

the_script = []
for line in f:
    the_script.append(line.strip())


# i is used for loop iterations.
i = 0
# p is used to control the print iterations.
p = 0
# This initial while loop will queue up the teleprompter before beginning to print text.
# This is helpful for when you are beginning to record.
while (p < len(the_script)) & ((p - i) != 11):
        print(the_script[p])
        p += 1
# The following line resets p, which is important for the teleprompter to know bug out.
p = i

# This will cause the program to wait until we start pressing the hotkey to begin.
keyboard.wait(hotkey)


# This While loop provides main functionality to the script. 
while i < len(the_script):
    # Types the text according to the script. Delay sets speed of each key.
    keyboard.write(the_script[i], delay=0.03)
    # The next two lines will fix the hotkey bug, as long as hotkey is set to shift.
    enterboard.press(Key.shift)
    enterboard.release(Key.shift)
    # The next two lines will automatically press enter, which is helpful so we don't manually need to do that.
    enterboard.press(Key.enter)
    enterboard.release(Key.enter)
    # Increase both iterations by 1 to match current script position.
    i += 1
    p += 1
    # Loop inside loop will make program less efficient, but since it isn't doing that much it should be fine.
    os.system("cls")
    # The != portion controls up to how many lines of text we want in the output box.
    while (p < len(the_script)) & ((p - i) != 10):
        print(the_script[p])
        p += 1
    # Reset p to i. This makes sure that the loop directly above this comment will run correctly when the next
    # line of text is output.
    p = i
    # Wait for the hotkey again.
    keyboard.wait(hotkey)

