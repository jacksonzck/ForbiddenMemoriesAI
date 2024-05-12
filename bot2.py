import pyautogui
import keyboard
import asyncio
from functools import partial
from time import sleep

def find_image(image_name: str) -> bool:
    try:
        pyautogui.locate(image_name)
        print(f"Found {image_name}!")
        return True
    except Exception:
        return False

def atDeckConstruction() -> bool:
    return find_image("Deck_Construct_Screen.png")

def atBattleSelect() -> bool:
    return find_image("FreeDuel.png")

def looking_at_battlefield() -> bool:
    return find_image("BattleBar.png") and find_image('LitYou.png')

def looking_at_hand() -> bool:
    return (not looking_at_battlefield()) and find_image('LitYou.png')

def cardInSlot(slot_number: int) -> bool:
    if not looking_at_battlefield():
        raise Exception
    match slot_number:
        case 1: return not find_image("CardSlot1.png")
        case 2: return not find_image("CardSlot2.png")
        case 3: return not find_image("CardSlot3.png")
        case 4: return not find_image("CardSlot4.png")
        case 5: return not find_image("CardSlot5.png")
    return False

def find_state() -> str:
    if atDeckConstruction(): return "deck_construction"
    if atBattleSelect(): return "at_battle_select"
    if looking_at_hand(): return "looking_at_hand"
    if looking_at_battlefield(): return "looking_at_battlefield"
    return "i_dunno"

async def run_bot():
    while True:
        print("HAHA PETER I AM RUNNING")
        await sleep(1)
    # TODO: Actual logic here (State Machine!)

async def main() -> None:
    print(f"Starting Bot")
    sleep(3)
    my_task = asyncio.create_task(coro=run_bot())
    def stop_running(_):
        print("NOW IS YOUR TIME TO DIE, TASK!")
        my_task.cancel()
    keyboard.hook_key("esc", stop_running)

if __name__ == "__main__":
    asyncio.run(main())