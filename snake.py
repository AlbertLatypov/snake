import time, sys
import os
import msvcrt   # не работает в принципе
from pynput.keyboard import Key, Controller, Listener
import keyboard
from functools import partial


def on_press(key):
    global k
    k = key
    print('{0} pressed'.format(
        key))


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released

with Listener(on_press=on_press,on_release=on_release) as listener: listener.join()


keyboard.hook(on_press)
print(k)
print('tut')


def print_pressed_keys(e):
    global k
    k = str(e.name)
    print(e.name)



    
'''
def returnkey(key):
    if key.name == "space":
        print('ssdpace')
    global i
    i=key.name
'''

keyboard.hook(print_pressed_keys)
print(k)
#a=keyboard.add_hotkey('w', print, args=['space was pressed'])
keyboard.wait()

'''
import msvcrt
while True:
  x = msvcrt.kbhit()
  if x:
    k = ord(msvcrt.getch())
    if k == 101:
      print("Нажата E")
'''

   
msvcrt.getch()
print(msvcrt.getch())

for z in range (1000):
    a = input()
    for i in range (10):
        for j in range (10):
            sys.stdout.write('|_')
        sys.stdout.write('\n')
    
'''
for i in range(10):
    sys.stdout.write('3')
    time.sleep(1)
'''




    
a = input()

if a == 'a':
    print('успех')
if a != 'a':
    print('неуспех')
