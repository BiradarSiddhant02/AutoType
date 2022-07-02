from pyautogui import press, typewrite, hotkey
from time import sleep, time

flag = 0


def check(ch):
    global flag
    if ch != "\n":
        typewrite(ch)
    if ch == "\n":
        if flag != 0:
            press('space')
            press('enter')
            hotkey('shift', 'home', 'home', 'backspace')
        else:
            press('enter')
    elif ch == "(" or ch == "[" or ch == "{":
        press('delete')
        if ch == "{":
            flag += 1
    elif ch == "}":
        flag -= 1


"""
    Put the code in cfile.c, change the window to chrome and place the cursor
    MOVE MOUSE TO TOP LEFT POSITION OF SCREEN TO STOP (FAILSAFE)
"""

for i in range(5, 0, -1):  # countdown of 5 seconds to change the window to chrome and place the cursor
    print(f"Starting in {i}")
    sleep(1)

start = time()
with open('cfile.c', 'r') as file:  # opens the file cfile.c to take lines from
    file_arr = file.read()

    for i, ch in enumerate(file_arr):
        check(ch)

stop = time()
print(f"Time elapsed: {round(stop-start, 2)}s")
