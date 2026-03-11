from telebot import types
from boot import *
from datetime import datetime, timedelta
import asyncio
def mods(bot):
    @bot.message_handler(regexp='Бан',chat_types=["supergroup","group"])
    @bot.message_handler(regexp='Ban',chat_types=["supergroup","group"])
    async def ban(message):
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        if (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message!=None:
            banner=message.reply_to_message.from_user
            status_banner=await bot.get_chat_member(message.chat.id,banner.id)
            if len(message.text)>3 and (status_banner):
                await bot.ban_chat_member(message.chat.id,banner.id)
                await bot.send_message(message.chat.id, f"Пользователь @{banner.username} забанен\nИнициатор {message.from_user.username} по причине {message.text[5:]}")
            elif len(message.text)==3:
                await bot.ban_chat_member(message.chat.id,banner.id)
                await bot.send_message(message.chat.id, f"Пользователь @{banner.username} забанен\nИнициатор {message.from_user.username}")
            else:
                await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал")
            #elif (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message==None:
                #banner=message.text.split()[1][1:]
                #status_banner=await bot.get_chat_member(chat,banner.id)
                #if len(message.text)>3 and (status_banner!="creator" or status_banner.status!="left"):
                #    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username} по причине {message.text.split()[1]}")
                #elif len(message.text)==3 and (status_banner!="creator" or status_banner.status!="left"):
                #    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username}")
                #else:
                #    await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал")
            #else:
                #await bot.send_message(message.chat.id, "Данная команда доступна только администрации и модерации")
    @bot.message_handler(regexp='Мут',chat_types=["supergroup","group"])
    @bot.message_handler(regexp='Mute',chat_types=["supergroup","group"])
    async def mute_user(message):
            #упоминание начиная с
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        if (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message!=None:
                banner=message.reply_to_message.from_user
                status_banner=await bot.get_chat_member(message.chat.id,banner.id)
                if len(message.text)>3:
                    await bot.ban_chat_member(message.chat.id,banner.id)
                    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username} по причине {message.text.split()[1]}")
                elif len(message.text)==3:
                    await bot.ban_chat_member(message.chat.id,banner.id)
                    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username}")
                else:
                    await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал")
            #elif (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message==None:
                #banner=message.text.split()[1][1:]
                #status_banner=await bot.get_chat_member(chat,banner.id)
                #if len(message.text)>3 and (status_banner!="creator" or status_banner.status!="left"):
                #    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username} по причине {message.text.split()[1]}")
                #elif len(message.text)==3 and (status_banner!="creator" or status_banner.status!="left"):
                #    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username}")
                #else:
                #    await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал")
            #else:
                #await bot.send_message(message.chat.id, "Данная команда доступна только администрации и модерации")
    @bot.message_handler(regexp='Варн',chat_types=["supergroup","group"])
    @bot.message_handler(regexp='Warn',chat_types=["supergroup","group"])
    async def warn_user(message):
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        match admin:
            case "administrator":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе")
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе")
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
            case "creator":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение самому себе")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение самому себе")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
            case "left":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе")
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе")
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе")
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано")
            case _:
                await bot.send_message(message.chat.id, "Данная команда доступна только администрации и модерации")