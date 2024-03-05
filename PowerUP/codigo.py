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
time.sleep(5)

