import subprocess
import time

from telethon import TelegramClient
import psutil

import personal_settings


def is_running_python_script(scriptName):
    """
    Checks whether a specific Python script is running

    :param scriptName: Script name
    :return: True if script is running, False if it doesn't
    """
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            continue
        if "python" in p.name():
            for item in p.cmdline():
                if scriptName in item:
                    return True
    return False


def pid_of_program_or_script(scriptName):
    """
    Defines the process ID of a Python script or program

    :param scriptName: Script/program name
    :return: process ID
    """
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            continue
        if "python" in p.name():
            for item in p.cmdline():
                if scriptName in item:
                    return p.pid
        else:
            if scriptName in p.name():
                return p.pid
    return -1


async def main():
    """
    Monitors telegram chat messages, if it sees "+",
    it starts the bot script, if it sees "-", it stops the bot and closes the game
    """
    while True:
        try:
            conf_message = await client.get_messages(personal_settings.CONTROL_CHAT_ID, limit=1)
        except ConnectionError:
            conf_message = '-'
            print('telegram connect error')
        if conf_message[0].text == '+':
            if not is_running_python_script('main.py'):
                subprocess.Popen(personal_settings.MAIN_PY_PATH)
            try:
                await client.send_read_acknowledge(personal_settings.CONTROL_CHAT_ID)
            except Exception:
                print('connection error')
        if conf_message[0].text == '-':
            if is_running_python_script('main.py'):
                try:
                    ps = psutil.Process(pid_of_program_or_script('main.py'))
                    ps.kill()
                    pr = psutil.Process(pid_of_program_or_script('Hearthstone.exe'))
                    pr.kill()
                except Exception:
                    print('already killed or wrong pid')
            try:
                await client.send_read_acknowledge(personal_settings.CONTROL_CHAT_ID)
            except Exception:
                print('connection error')
        time.sleep(60)


def repeat():
    """
    Restarts execution if errors occur
    """
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception:
        repeat()


client = TelegramClient(personal_settings.SESSION_NAME, personal_settings.API_ID,
                        personal_settings.API_HASH, system_version='4.16.30-vxCUSTOM')

repeat()
