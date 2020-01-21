import time
import os
import threading
import sys
from colorama import *
from pynput.keyboard import Key,Listener
on=True
counter=0
laps=''''''
killed=False
cur=1
print(Fore.GREEN)
os.system('color a')
def timer():
    global counter
    while True:
        if on:
            d=divmod(counter,60)
            os.system('cls')
            print(laps)
            print('Time : '+str(d[0])+' min '+str(d[1])+' sec')
            time.sleep(1.0)
            counter+=1
        if killed:
            break
def lap():
    global cur,laps
    laps+='\nLap '+str(cur)+' : '+str(counter)+' secs'
    cur+=1
def reset():
    global counter
    print('Time Reset')
    counter=0
def stop():
    global on,process1,process2,killed
    killed=True
    on=False
    print('Stopped')
    process1.join(0);process2.join(0)
    time.sleep(2.0)
    sys.exit(0)
def play_pause():
    global on
    print('Paused')
    on=not(on)
def pressed(key):
    if killed:
        return False
    {'p':play_pause,
        's':stop,
        'r':reset,
        'l':lap,
        }.get(str(key)[1],ff)()
def released(key):
    pass
def ff():
    pass
def listen():
    try:
        with Listener(on_press=pressed,on_release=released) as listener:
            listener.join()
    except:
        with Listener(on_press=pressed,on_release=released) as listener:
            listener.join()
process1=threading.Thread(target=timer)
process2=threading.Thread(target=listen)
process1.start()
process2.start()
