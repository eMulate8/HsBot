import random
import time

import numpy as np
import pyautogui

import personal_settings
from utility_functions import click, check_client_active, check_text


def do_nothing():
    """
    Presence simulation so that the client does not disconnect due to inactivity
    """
    print('do_nothing')
    time.sleep(60)
    x_x = np.random.randint(130, 180)
    y_y = np.random.randint(200, 525)
    t1 = random.triangular(1, 2)
    pyautogui.moveTo(565, 510, duration=t1)
    pyautogui.moveTo(550, 340, duration=t1)
    pyautogui.moveTo(680, 510, duration=t1)
    pyautogui.moveTo(680, 335, duration=t1)
    pyautogui.moveTo(800, 510, duration=t1)
    pyautogui.moveTo(550, 340, duration=t1)
    pyautogui.moveTo(x_x, y_y, duration=t1)
    if check_client_active():
        return None
    click()
    click()


def game():
    """
    Actions after the start of the match
    """

    t1 = random.triangular(1, 2)
    while not check_text('ок', 665, 595, 45, 22, 0, 0, 45, 0, 0, 255, True):
        time.sleep(1)
        if check_client_active():
            return None
    pyautogui.moveTo(685, 605, duration=t1)
    click()
    time.sleep(5)

    for i in range(personal_settings.NUMBER_OF_INACTIVITY):
        do_nothing()

    while not check_text('шелкните,', 420, 720, 185, 30, 0, 0, 45, 0, 0, 255, True) and \
            not check_text('отступриь', 283, 682, 57, 12, 0, 0, 100, 255, 135, 255, True):
        pyautogui.moveTo(1115, 350, duration=t1)
        if check_client_active():
            return None
        click()
        time.sleep(5)

    click()
    time.sleep(2)
    click()
    time.sleep(2)


def menu_actions():
    """
    Actions after the match
    """
    t1 = random.triangular(1, 2)
    time.sleep(15)
    while not check_text('отступриь', 283, 682, 57, 12, 0, 0, 100, 255, 135, 255, True):
        time.sleep(1)
        if check_client_active():
            return None

    pyautogui.moveTo(315, 690, duration=t1)
    if check_client_active():
        return None
    click()
    time.sleep(1)
    pyautogui.moveTo(600, 460, duration=t1)
    if check_client_active():
        return None
    click()
    time.sleep(1)


def play_from_main_menu():
    """
    Actions to switch from the main menu to the desired mode
    """
    t1 = random.triangular(1, 2)
    pyautogui.moveTo(690, 400, duration=t1)
    click()
    while not check_text('вызрать', 900, 515, 150, 25, 0, 0, 230, 0, 0, 255, False):
        time.sleep(1)
        if check_client_active():
            return None
    pyautogui.moveTo(580, 200, duration=t1)
    click()
    time.sleep(1)
    pyautogui.moveTo(975, 530, duration=t1)
    click()


def active_run():
    """
    Аctions if the adventure was active
    """
    t1 = random.triangular(1, 2)
    retired_check_times = 10
    retired_check = False
    while not check_text('отступриь', 283, 682, 57, 12, 0, 0, 100, 255, 135, 255, True):
        time.sleep(1)
        retired_check_times -= 1
        if retired_check_times == 0:
            break
    else:
        retired_check = True

    if retired_check:
        time.sleep(1)
        pyautogui.moveTo(315, 690, duration=t1)
        if check_client_active():
            return None
        click()
        time.sleep(1)
        pyautogui.moveTo(600, 460, duration=t1)
        if check_client_active():
            return None
        click()
        time.sleep(1)
    else:
        pyautogui.moveTo(800, 590, duration=t1)
        if check_client_active():
            return None
        click()
        game()
        menu_actions()


def inactive_run():
    """
    Аctions if the adventure was inactive
    """
    t1 = random.triangular(1, 2)
    while not check_text('о герое', 950, 15, 85, 15, 0, 0, 240, 0, 0, 255, False):
        time.sleep(1)
        if check_client_active():
            return None

    pyautogui.moveTo(630, 550, duration=t1)
    if check_client_active():
        return None
    click()
    time.sleep(4)
    while not check_text('вызрать', 935, 625, 120, 20, 0, 0, 230, 0, 0, 255, False):
        time.sleep(1)
        if check_client_active():
            return None

    pyautogui.moveTo(1000, 645, duration=t1)
    click()
    time.sleep(8)
    pyautogui.moveTo(550, 640, duration=t1)
    click()
    time.sleep(2)
    click()
    time.sleep(2)
    click()
    time.sleep(2)
    while not check_text('играть', 740, 570, 125, 25, 0, 0, 0, 0, 0, 255, True):
        time.sleep(1)
        if check_client_active():
            return None

    pyautogui.moveTo(800, 590, duration=t1)
    if check_client_active():
        return None
    click()
    game()
    menu_actions()


def adventures_run():
    """
    Selecting a hero and starting the game in adventure mode
    """
    t1 = random.triangular(1, 2)
    while not check_text('книга', 400, 10, 70, 30, 0, 0, 240, 0, 0, 255, False):
        if check_client_active():
            return None
        time.sleep(1)

    while not check_text('колода', 1020, 15, 77, 15, 0, 0, 0, 255, 125, 255, True) and \
            not check_text('о герое', 950, 15, 85, 15, 0, 0, 240, 0, 0, 255, False):
        pyautogui.moveTo(990, 635, duration=t1)
        if check_client_active():
            return None
        click()

    time.sleep(12)

    if check_text('играть', 740, 570, 125, 25, 0, 0, 0, 0, 0, 255, True):
        active_run()
    else:
        inactive_run()
