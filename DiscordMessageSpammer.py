from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from colorama import Fore, init
import pytesseract
import pyautogui
import time
import cv2
import os
init()

os.system('title Discord Message Spammer - By Mozaki')

print(Fore.LIGHTRED_EX+"""  ___  _                   _   __  __                            ___                                
 |   \(_)___ __ ___ _ _ __| | |  \/  |___ ______ __ _ __ _ ___  / __|_ __  __ _ _ __  _ __  ___ _ _ 
 | |) | (_-</ _/ _ \ '_/ _` | | |\/| / -_|_-<_-</ _` / _` / -_) \__ \ '_ \/ _` | '  \| '  \/ -_) '_|
 |___/|_/__/\__\___/_| \__,_| |_|  |_\___/__/__/\__,_\__, \___| |___/ .__/\__,_|_|_|_|_|_|_\___|_|  
                                                     |___/          |_|                             
""")

loggedin = False

messageuser = input(Fore.RESET+" DM link: ")
message = input(" Text you want to spam: ")
username = input(" Discord email or phone number: ")
password = input(" Discord password: ")

user1 = 'C:/Users/'
user2 = os.getlogin()
user3 = '/AppData/Local/Programs/Python/Python310/chromedriver.exe'

driver = webdriver.Chrome(executable_path=user1 +user2 +user3)

driver.get('https://discord.com/login')


while True == True:
    time.sleep(0.6)
    checkpageload = pyautogui.screenshot('discordload.png')
    checkpageloadread = cv2.imread('discordload.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(checkpageloadread, config=config)
    text = text.split('\n')
    if 'Welcome back!' in text:
        time.sleep(0.3)
        pyautogui.write(username)

        loginbox = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
        loginbox.click()

        pyautogui.write(password)

        clickloginbutton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]")
        clickloginbutton.click()
        loggedin = True
        time.sleep(1.5)
        driver.get(messageuser)
        sendmessage = True
        while sendmessage == True:
            time.sleep(0.1)
            pyautogui.write(message)
            pyautogui.press('enter')