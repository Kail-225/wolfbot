import asyncio
from telebot import types
from boot import *
from datetime import datetime, timedelta
def coms(bot):
    @bot.message_handler(commands=['start'],chat_types=['private'])
    async def start(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://wolfbot.ru')
        btn2 = types.InlineKeyboardButton(text="Добавить бота",url="https://t.me/WoIlFbOt?startgroup=wolfbot&admin=change_info+restrict_members+delete_messages+pin_messages+invite_users")
        markup.add(btn1,btn2)
        sup=support()
        await bot.send_message(message.chat.id,f"Помощь по работе бота wolfbot.\nТехническая поддержка:\n{sup}",reply_markup = markup, parse_mode='Markdown',disable_web_page_preview = True)
    @bot.message_handler(regexp="Кто я|I'm",chat_types=["supergroup","group"])
    async def info_user(message):
        info=search_info_user(message.from_user.id,message.chat.id)
        if info[5]==None:
            guild="Не состоит"
        else:
            guild=search_info_guild(info[5])[0][1]
        status=await bot.get_chat_member(message.chat.id,message.from_user.id)
        if info[6]==None:
            inv="Пусто"
        else:
            inv=info[6]
        await bot.send_message(message.chat.id, f"Информация о пользователе {status.user.first_name}\nСтатус: {status.status}\nМонеты: {info[4]}\nКоличество предупреждений: {info[7]}\nГильдия: {guild}\nИнвентарь: {inv}",reply_to_message_id=message.id)
    @bot.message_handler(regexp='Кто админы|Admins',chat_types=["supergroup","group"])
    async def admins(message):
        admins_chat=""
        info=await bot.get_chat_administrators(message.chat.id)
        for i in info:
            admins_chat+=f"[{i.user.first_name}](https://t.me/{i.user.username})\n"
        await bot.send_message(message.chat.id, f"Список администраторов:\n{admins_chat}",parse_mode='Markdown', reply_to_message_id=message.id, disable_web_page_preview = True)
    @bot.chat_member_handler()
    @bot.message_handler(content_types=['new_chat_members'])
    async def nu(message):
        name=await bot.get_me()
        if name.id==message.json["new_chat_member"]["id"]:
            add_group(message.chat.id,message.chat.title)
        elif message.json["new_chat_member"]["is_bot"]==True:
            pass
        else:
            check=search_filter(message.from_user.id,message.from_user.username)
            if check==None:
                await bot.restrict_chat_member(message.chat.id,message.from_user.id, can_send_messages=False)
                markup = types.InlineKeyboardMarkup()
                btn1 = types.InlineKeyboardButton(text='Да',callback_data="Ответ_Да")
                btn2 = types.InlineKeyboardButton(text='Нет',callback_data="Ответ_Нет")
                markup.add(btn1,btn2)
                mes_test=await bot.send_message(message.chat.id, f"@{message.from_user.username}, Ты атеист? На ответ две минуты", reply_markup = markup, parse_mode='Markdown', disable_web_page_preview = True)
                time_test=datetime.now()+timedelta(minutes=2)
                answer=0
                while datetime.now()<time_test and answer==0:
                    @bot.callback_query_handler(lambda call: call.data.startswith('Ответ_'))
                    async def handle_callback(call):
                        global answer
                        match call.data:
                            case 'Ответ_Да':
                                if call.from_user.id==message.from_user.id:
                                    answer=1
                                    await bot.restrict_chat_member(message.chat.id,message.from_user.id, can_send_messages=True)
                                    role=await bot.get_chat_member(message.chat.id,message.from_user.id)
                                    add_user(message.from_user.id,message.from_user.username,message.chat.id,role)
                                    await bot.delete_message(message.chat.id, mes_test.message_id)
                                    await bot.delete_message(message.chat.id, message.id)
                            case 'Ответ_Нет':
                                if call.from_user.id==message.from_user.id:
                                    answer=1
                                    await bot.restrict_chat_member(message.chat.id,message.from_user.id, can_send_messages=True)
                                    role=await bot.get_chat_member(message.chat.id,message.from_user.id)
                                    add_user(message.from_user.id,message.from_user.username,message.chat.id,role)
                                    await bot.delete_message(message.chat.id, mes_test.message_id)
                                    await bot.delete_message(message.chat.id, message.id)
                    await asyncio.sleep(10)
                if answer==0:
                    await bot.delete_message(message.chat.id, mes_test.message_id)
                    await bot.kick_chat_member(message.chat.id,message.from_user.id)
                    await bot.delete_message(message.chat.id, message.id)
            else:
                await bot.ban_chat_member(message.chat.id,message.from_user.id)
                await bot.delete_message(message.chat.id, message.id)
    @bot.message_handler(regexp="Варны|Warns",chat_types=['supergroup','group'])
    async def warns(message):
        count_warns=search_warn(message.from_user.id,message.chat.id)
        await bot.send_message(message.chat.id,f"Текущее количество варнов: {count_warns}",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Инвентарь|Items",chat_types=['supergroup','group'])
    async def invent(message):
        inv=search_items(message.from_user.id,message.chat.id)
        if inv==None:
            await bot.send_message(message.chat.id,f"Инвентарь:\nНичего нет",reply_to_message_id=message.id)
        else:
            inv=inv.replace(",","\n")
            inv=inv.replace(":",". Количество: ")
            await bot.send_message(message.chat.id,f"Инвентарь:\n{inv}",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Магазин|Magazin",chat_types=['supergroup','group'])
    async def magazin(message):
        mag=search_magazin()
        if mag==None or str(mag)=="[]":
            await bot.send_message(message.chat.id,f"Ассортимент магазина:\nВсё разобрали",reply_to_message_id=message.id)
        else:
            assort=""
            for i in mag:
                assort+=f"{i[1]}. Количество: {i[2]}/{i[3]}. Цена: {i[4]} монет\n"
            await bot.send_message(message.chat.id,f"Ассортимент магазина:\n{assort}",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Купить предмет|Buy item",chat_types=['supergroup','group'])
    async def buy_item(message):
        item=""
        for i in message.text.split()[2:-1]:
            item+=i+""
        item=item.lower().capitalize()
        sell_count=search_item(item)
        match sell_count:
            case None:
                await bot.send_message(message.chat.id,f"Данного товара нет в магазине",reply_to_message_id=message.id)
            case _:
                count=int(message.text.split()[-1])
                if count>int(sell_count[2]):
                    await bot.send_message(message.chat.id,f"Вы не можете купить больше остатка",reply_to_message_id=message.id)
                elif count==0:
                    await bot.send_message(message.chat.id,f"Вы не можете купить 0 единиц товара",reply_to_message_id=message.id)
                else:
                    money=search_money(message.from_user.id,message.chat.id)
                    if money>=count*int(sell_count[4]):
                        minus_money(message.from_user.id,message.chat.id,count*int(sell_count[4]))
                        minus_item(item,count)
                        add_item(message.from_user.id,message.chat.id,item,count)
                        await bot.send_message(message.chat.id,f"Вы успешно купили {item} в количестве {count} за {count*int(sell_count[4])} монет",reply_to_message_id=message.id)
                    else:
                        await bot.send_message(message.chat.id,f"У вас недостаточно монет для покупки",reply_to_message_id=message.id)