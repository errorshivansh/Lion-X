import os
os.system("pip install telethon")
import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


okk = input("Enter 6969 to continue: ")
if okk == "6969":
    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print(client.session.save())
        client.send_message("me", client.session.save())
        client.send_message("me", "Above is your #LIONX_SESSION \nPaste this string in Heroku Var.\n\n[Team ](t.me/The_LionX)")

else:
    print("chalaa jaa bhosdike")
