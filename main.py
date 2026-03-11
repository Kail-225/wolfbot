import asyncio
from telebot.async_telebot import AsyncTeleBot
from boot import *
from commands import *
t=access()["tg"]
bot = AsyncTeleBot(t)
coms(bot)
async def start():
    name=await bot.get_me()
    await bot.infinity_polling(print(f"Logged in as {name.first_name}"), interval=0,logger_level=None,skip_pending=True)
asyncio.run(start())