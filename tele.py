import asyncio,signal,sys
from telebot.async_telebot import AsyncTeleBot
from boot import *
from commands import coms
from mods import mods
from messages import messages
from guilds import guild
from personal import pers
t=access()["tg"]
bot=AsyncTeleBot(t)
async def reset_magazin():
    while(True):
        await asyncio.sleep(604800)
        update_magazin()

async def minusday_vip():
    while(True):
        await asyncio.sleep(86400)
        update_vip(None,1,False)

con()
coms(bot)
mods(bot)
guild(bot)
pers(bot)
messages(bot)
def signal_handler(sig,frame):
    write_log("Бот был отключён")
    sys.exit(0)
signal.signal(signal.SIGINT,signal_handler)
async def start():
    task1=asyncio.create_task(reset_magazin())
    task2=asyncio.create_task(minusday_vip())
    write_log("Бот запущен")
    name=await bot.get_me()
    print(f"Logged in as {name.first_name}")
    await task1
    await task2
    await bot.polling(non_stop=True, interval=0, skip_pending=True)
code=input("Введите код: ")
if code=="1010":
    asyncio.run(start())