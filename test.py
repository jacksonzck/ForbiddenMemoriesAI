#import keyboard
from time import sleep
from pynput.keyboard import Controller
sleep(3)
keyboard = Controller()
keyboard.type('TEST')

#keyboard.write("TEST")