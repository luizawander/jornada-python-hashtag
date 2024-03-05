import pyautogui
import time

pyautogui.PAUSE= 0.5

##acessando chrome 
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#dar um delay
time.sleep(1)

pyautogui.click(x=539, y=382)
pyautogui.write("luiza@gmail.com")

pyautogui.press("tab")

pyautogui.write("auauau")

pyautogui.click(x=665, y=538)
