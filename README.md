# HsBot
 Bot for Hearthstone
 
The bot earns scrolls, thereby increasing the levels in the rewards feed, for which various bonuses are awarded. The bot does NOT play with real people to reduce the risk of account bans. Farming of scrolls occurs in adventure mode (previously there was farming in mercenaries, but the reward for the battle was significantly reduced there).

The bot uses screen coordinates for its work; using them, it finds the necessary objects with which it interacts using the mouse cursor. Therefore, it is very important that nothing unnecessary appears on the screen during its operation. It is also not advisable to move the mouse while working.

The bot may get stuck at some stage of its work or stop working; this happens due to the bot’s use of the game interface, which may change over time.

The bot is configured to work with the Russian Hearthstone client, in full screen mode with a screen resolution of 1366x768. Battle.net must also be opened in full screen.

To work with clients in other languages, you need to replace Russian words in the bot code with words that are in the same place in the game interface in another language.

To work in a different resolution, you need to change all object coordinates.

The main.py requires the following modules that are not included in the list of standard modules: numpy, pyautogui, mss, opencv-python, pytesseract, fuzzywuzzy, wmi

You also need to install pytesseract packege for your system (by default, the bot needs Russian language package to work)
https://tesseract-ocr.github.io/tessdoc/Installation.html

The bot can be launched directly from the main.py script, but can be launched using remote_acc.py which allows you to start and stop the bot by sending a telegram chat message. To do this, you will need to install two more modules: psutil, telethon.

You have to get Telegram api keys:
			 
	- Login to your Telegram account (https://my.telegram.org/auth) with the phone number of the developer account to use.
	- Click under API Development tools.
	- A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
	- Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

You need a telegram session file, which will be created as soon as you connect your telegram account to the bot.

Fill in the settings.py file with the corresponding data.



