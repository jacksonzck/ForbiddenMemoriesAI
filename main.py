import keyboard # Can't read keys in my window manager
from time import sleep
from voicebox import SimpleVoicebox
from voicebox.tts import gTTS
from voicebox.effects import Vocoder, Normalize
# import pyscreenshot as ImageGrab # Doesn't work because of Wayland
# import uinput
from pynput.keyboard import Key, Controller
import sys
import os

PIXEL_LOCATION = (2044, 1257)

pynput_keyboard: Controller = Controller()

voicebox = SimpleVoicebox(
    tts=gTTS(),
    effects=[Vocoder.build(), Normalize()],
)

#voicebox.say("Test Test Halleulah!!")
do_i_quit = [False] 

def write_stuff(string):
    for character in string:
        if do_i_quit[0]:
            raise SystemExit
        sleep(0.5)
        match character:
            #case 'l':
            #    device.emit_click(uinput.KEY_L)
            #case 'k':
            #    device.emit_click(uinput.KEY_K)
            case '<':
                pynput_keyboard.press(Key.left)
                sleep(0.03)
                pynput_keyboard.release(Key.left)
            case '>': 
                pynput_keyboard.press(Key.right)
                sleep(0.03)
                pynput_keyboard.release(Key.right)
            case 'E':
                pynput_keyboard.press(Key.enter)
                sleep(0.1)
                pynput_keyboard.release(Key.enter)
                #device.emit_click(uinput.KEY_ENTER)
            case default:
                pynput_keyboard.press(character)
                sleep(0.1)
                pynput_keyboard.release(character)
        #keyboard.write(character)

def main():
    sleep(3)
    def quit_program(_kk): 
        print("I like beef!")
        do_i_quit[0] = True
    keyboard.hook_key("esc", quit_program)
    while not do_i_quit[0]:
        sleep(1)
        write_stuff("kkkkkkkl")
        sleep(1)
        write_stuff("kk")
        for _ in range(5):
            sleep(0.5)
            write_stuff("kk")
            write_stuff('<')
        for _ in range(5):
            write_stuff("kk")
            sleep(0.5)
            write_stuff("kk")
            write_stuff(">")
        write_stuff('E')
        sleep(4)
        pass
    # Look at some pixel to realize what state we're in
    # Might need to sample multiple pixels over a period of time for reliability???
    #while True:
    #voicebox.say("NOMING SCREEN IN 3 SECONDS")
    #sleep(3)
    #print(str(ImageGrab.grab().getpixel(PIXEL_LOCATION)))
    #voicebox.say("THANK YOU NEXT NEXT")
    #sleep(1)


    # State 0: Waiting for the game to do stuff
    # Just like, sleep or something and try again

    # State 1: In a battle/
    # Mash the K key
    pass

if __name__ == "__main__":
    main()