import time
from ctypes import windll, create_unicode_buffer
import os

import numpy as np
import pyautogui
import mss
import cv2
import pytesseract
from fuzzywuzzy import fuzz
import mss.tools
import wmi

import personal_settings

pytesseract.pytesseract.tesseract_cmd = personal_settings.PYTESSERACT_PATH


def terminate_client():
    """
    Kill game's process(es)
    """
    c = wmi.WMI()
    for process in c.Win32_Process(name="Battle.net.exe"):
        print(process.ProcessId, process.Name)
        try:
            process.Terminate()
        except Exception:
            print('already killed')

    for process in c.Win32_Process(name="Hearthstone.exe"):
        print(process.ProcessId, process.Name)
        try:
            process.Terminate()
        except Exception:
            print('already killed')


def run_hs():
    """
    Launches the game client at the specified path
    """
    terminate_client()
    time.sleep(15)
    print('run hs')
    os.startfile(personal_settings.GAME_CLIENT_PATH)

    print_one_time = True
    while not check_text('играть', 115, 605, 85, 25, 0, 0, 100, 100, 255, 255, True):
        if print_one_time:
            print('Проверяю кнопку играть в батл нет')
            print_one_time = False
        time.sleep(1)

    while True:
        time.sleep(3)
        pyautogui.moveTo(160, 620, duration=0.1)
        click()
        time.sleep(3)
        if check_text('закрыть', 655, 605, 73, 20, 0, 0, 0, 255, 255, 170, False):
            pyautogui.moveTo(695, 615, duration=0.1)
            click()

        if check_text('режимы', 630, 390, 110, 20, 17, 0, 0, 90, 163, 140, False):
            break


def get_foreground_window_title():
    """
    Get active window title
    :return: window title or None
    """
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    if buf.value:
        return buf.value
    return None


def click():
    """
    Left mouse click
    """
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()


def check_text(text, screen_x, screen_y, width, height, a1, a2, a3, b1, b2, b3, use_bitwise_and):
    """
        Processing a screen area;
        in the find_color mode, a specified color is searched;
        in the grab_text and grab_digit modes, text or numbers are captured from the area;
        in the check_text mode, the text in the area is checked for compliance with a given pattern

        :param screen_x: x coordinates of the upper left corner of the treated area on the screen
        :param screen_y: y coordinates of the upper left corner of the treated area on the screen
        :param width: width of the treated area on the screen
        :param height: height of the treated area on the screen
        :param a1: lower border of hsv
        :param a2: lower border of hsv
        :param a3: lower border of hsv
        :param b1: upper border of hsv
        :param b2: upper border of hsv
        :param b3: upper border of hsv
        :param text: text for search
        :param use_bitwise_and: uses cv2.bitwise_and or not
        :return: True if the texts matches, False if its don't,
        """
    mon = {"top": screen_y, "left": screen_x, "width": width, "height": height}

    lower_color = np.array([a1, a2, a3])
    upper_color = np.array([b1, b2, b3])

    sct = mss.mss()
    img = np.asarray(sct.grab(mon))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    if use_bitwise_and:
        res = cv2.bitwise_and(img, img, mask=mask)
        rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    else:
        rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

    pcm6 = pytesseract.image_to_string(rgb, lang='rus', config='--psm 6')
    pcm7 = pytesseract.image_to_string(rgb, lang='rus', config='--psm 7')

    if (((fuzz.ratio(pcm6.lower(), text.lower())) > 50 or (fuzz.ratio(pcm7.lower(), text.lower())) > 50)
            or (text.lower() in pcm6.lower() or text.lower() in pcm7.lower())):
        return True

    else:
        return False


def check_client_active():
    """
    Check if the game is running and two options for messages when the game loses connection
    :return: True if game is NOT running or disconnected, False if game is running
    """
    window_name = get_foreground_window_title()
    if window_name != 'Hearthstone':
        flag = True
    else:
        flag = False
        if check_text('вы сейчас', 510, 390, 190, 40, 0, 0, 0, 255, 130, 150, True):
            terminate_client()
            flag = True
        if check_text('закрыто', 450, 330, 440, 100, 0, 0, 75, 0, 0, 255, False):
            terminate_client()
            flag = True
    return flag
