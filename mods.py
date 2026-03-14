from telebot import types
from boot import *
def mods(bot):
    @bot.message_handler(regexp='Бан|Ban',chat_types=["supergroup","group"])
    async def ban(message):
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        if (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message!=None:
            banner=message.reply_to_message.from_user
            status_banner=await bot.get_chat_member(message.chat.id,banner.id)
            if len(message.text)>3 and (status_banner):
                await bot.ban_chat_member(message.chat.id,banner.id)
                await bot.send_message(message.chat.id, f"Пользователь @{banner.username} забанен\nИнициатор {message.from_user.username} по причине {message.text[5:]}", reply_to_message_id=message.id)
            elif len(message.text)==3:
                await bot.ban_chat_member(message.chat.id,banner.id)
                await bot.send_message(message.chat.id, f"Пользователь @{banner.username} забанен\nИнициатор {message.from_user.username}", reply_to_message_id=message.id)
            else:
                await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал", reply_to_message_id=message.id)
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
    @bot.message_handler(regexp='Мут|Mute',chat_types=["supergroup","group"])
    async def mute_user(message):
            #упоминание начиная с
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        if (admin.status=="administrator" or admin.status=="creator" or admin.status=="left") and message.reply_to_message!=None:
                banner=message.reply_to_message.from_user
                status_banner=await bot.get_chat_member(message.chat.id,banner.id)
                if len(message.text)>3:
                    await bot.ban_chat_member(message.chat.id,banner.id)
                    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username} по причине {message.text.split()[1]}", reply_to_message_id=message.id)
                elif len(message.text)==3:
                    await bot.ban_chat_member(message.chat.id,banner.id)
                    await bot.send_message(message.chat.id, f"Пользователь @{banner.username} отправлен на колыму\nИнициатор {message.from_user.username}", reply_to_message_id=message.id)
                else:
                    await bot.send_message(message.chat.id, f"Вы не можете забанить создателя группы, анонимного администратора или канал", reply_to_message_id=message.id)
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
    @bot.message_handler(regexp='Варн|Warn',chat_types=["supergroup","group"])
    async def warn_user(message):
        admin=await bot.get_chat_member(message.chat.id,message.from_user.id)
        match admin:
            case "administrator":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе", reply_to_message_id=message.id)
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю", reply_to_message_id=message.id)
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            user_warns=search_warn(user,message.chat.id)
                            limit=search_warn_group(message.chat.id)
                            if user_warns==limit:
                                #await bot.
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе", reply_to_message_id=message.id)
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю")
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            search_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
            case "creator":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение самому себе", reply_to_message_id=message.id)
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение самому себе", reply_to_message_id=message.id)
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
            case "left":
                if message.reply_to_message!=None:
                    user=message.reply_to_message.from_user.id
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе", reply_to_message_id=message.id)
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю", reply_to_message_id=message.id)
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
                else:
                    user=search_username(message.split()[1])
                    status_user=await bot.get_chat_member(message.chat.id,user)
                    match status_user:
                        case "administrator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение другому администратору или самому себе", reply_to_message_id=message.id)
                        case "creator":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение создателю", reply_to_message_id=message.id)
                        case "left":
                            await bot.send_message(message.chat.id, "Вы не можете выдать предупреждение анонимному администратору или самому себе", reply_to_message_id=message.id)
                        case _:
                            add_warn(user,message.chat.id)
                            await bot.send_message(message.chat.id, "Предупреждение выдано", reply_to_message_id=message.id)
            case _:
                await bot.send_message(message.chat.id, "Данная команда доступна только администрации и модерации", reply_to_message_id=message.id)