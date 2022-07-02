from pyautogui import press, typewrite, hotkey
from time import sleep, time
from multiprocessing import Process
import os
import pynput

flag = 0
# f = open("typed.c", 'w')
# f.close()
# os.system("Notepad typed.c")

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



def Writer():


    # os.system("del typed.c")
    # os.system("new-item typed.c")
    
    start = time()
    with open('cfile.c', 'r') as file:  # opens the file cfile.c to take lines from
        file_arr = file.read()                                         

        for i, ch in enumerate(file_arr):
            check(ch)

    stop = time()
    print(f"Time elapsed: {round(stop-start, 2)}s")
    
def file_open():
    # f = open("typed.c", 'w')
    # f.close()
    pass
   
def window_opener():
    os.system("Notepad typed.c")    
    
if __name__ == "__main__":

    P = Process(target = file_open)
    Q = Process(target = Writer)
    R = Process(target = window_opener)

    Q.start()
    P.start()
    R.start()
        
    Q.join()
    P.join()
    R.join()
    
    
