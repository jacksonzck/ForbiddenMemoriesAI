import keyboard
from time import sleep
from voicebox import SimpleVoicebox
from voicebox.tts import gTTS
from voicebox.effects import Vocoder, Normalize
import pyscreenshot as ImageGrab

PIXEL_LOCATION = (2044, 1257)

voicebox = SimpleVoicebox(
    tts=gTTS(),
    effects=[Vocoder.build(), Normalize()],
)

#voicebox.say("Test Test Halleulah!!")

def main():
    # Look at some pixel to realize what state we're in
    # Might need to sample multiple pixels over a period of time for reliability???
    #while True:
    voicebox.say("NOMING SCREEN IN 3 SECONDS")
    print(str(ImageGrab.grab().getpixel(PIXEL_LOCATION)))
    voicebox.say("THANK YOU NEXT NEXT")
    sleep(1)


    # State 0: Waiting for the game to do stuff
    # Just like, sleep or something and try again

    # State 1: In a battle/
    # Mash the K key
    pass

if __name__ == "__main__":
    main()