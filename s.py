import time

import keyboard as keyboard
import pyautogui
import pyperclip
from googletrans import Translator

translator = Translator()


def main(textarea_old, id):
        pyperclip.copy('#'+textarea_old)
        pyautogui.click(1150, 1030, button='left')
        keyboard.press_and_release('ctrl + v')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'x')
        time.sleep(0.5)
        pyautogui.click(1050, 1030, button='left')
        time.sleep(0.5)
        pyautogui.click(300, 50)
        pyautogui.click()
        pyautogui.click()
        pyautogui.typewrite(f'http://127.0.0.1:8000/api/v1/docs/copilot/{id}/')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.click(3000, 1000, button='left')
        pyautogui.click(600, 800)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.click(1650, 880)



