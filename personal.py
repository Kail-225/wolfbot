from telebot import types
from boot import *
personal_group=-1002446031178
def pers(bot):
    @bot.message_handler(regexp="Выдать деньги",chat_types=['supergroup','group'])
    async def give_money(message):
        match message.chat.id:
            case _ if personal_group==message.chat.id:
                role=search_personal(message.from_user.id)
                if role==None:
                    await bot.send_message(message.chat.id,"Вы не являетесь сотрудником поддержки",reply_to_message_id=message.id)
                else:
                    text=message.text.split("  ")
                    match len(text):
                        case 5:
                            user=text[1]
                            group=text[2]
                            money=int(text[3])
                            reason=text[4]
                            add_money(user,group,money)
                            write_log(f'Сотрудник под id {message.from_user.id} выдал {money} монет пользователю под id {user} в группу {group} по причине "{reason}"')
                            await bot.send_message(message.chat.id,"Монеты выданы",reply_to_message_id=message.id)
                        case 4:
                            if message.reply_to_message==None:
                                user=text[1]
                                group=text[2]
                                money=int(text[3])
                                add_money(user,group,money)
                                write_log(f'Сотрудник под id {message.from_user.id} выдал {money} монет пользователю под id {user} в группу {group}')
                                await bot.send_message(message.chat.id,"Монеты выданы",reply_to_message_id=message.id)
                            else:
                                user=message.reply_to_message.from_user.id
                                group=text[1]
                                money=int(text[2])
                                reason=text[3]
                                add_money(user,group,money)
                                write_log(f'Сотрудник под id {message.from_user.id} выдал {money} монет пользователю под id {user} в группу {group} по причине "{reason}"')
                                await bot.send_message(message.chat.id,"Монеты выданы",reply_to_message_id=message.id)
                        case 3:
                            user=message.reply_to_message.from_user.id
                            group=text[1]
                            money=int(text[2])
                            add_money(user,group,money)
                            write_log(f'Сотрудник под id {message.from_user.id} выдал {money} монет пользователю под id {user} в группу {group}')
                            await bot.send_message(message.chat.id,"Монеты выданы",reply_to_message_id=message.id)
            case _:
                await bot.send_message(message.chat.id,"Данная команда доступна только в группе поддержки",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Забрать деньги",chat_types=['supergroup','group'])
    async def fetch_money(message):
        match message.chat.id:
            case _ if personal_group==message.chat.id:
                role=search_personal(message.from_user.id)
                if role==None:
                    await bot.send_message(message.chat.id,"Вы не являетесь сотрудником поддержки",reply_to_message_id=message.id)
                else:
                    text=message.text.split("  ")
                    match len(text):
                        case 5:
                            user=text[1]
                            group=text[2]
                            money=int(text[3])
                            reason=text[4]
                            minus_money(user,group,money)
                            write_log(f'Сотрудник под id {message.from_user.id} забрал {money} монет у пользователя под id {user} из группы {group} по причине "{reason}"')
                            await bot.send_message(message.chat.id,"Монеты забраны",reply_to_message_id=message.id)
                        case 4:
                            if message.reply_to_message==None:
                                user=text[1]
                                group=text[2]
                                money=int(text[3])
                                minus_money(user,group,money)
                                write_log(f'Сотрудник под id {message.from_user.id} забрал {money} монет у пользователя под id {user} из группы {group}')
                                await bot.send_message(message.chat.id,"Монеты забраны",reply_to_message_id=message.id)
                            else:
                                user=message.reply_to_message.from_user.id
                                group=text[1]
                                money=int(text[2])
                                reason=text[3]
                                minus_money(user,group,money)
                                write_log(f'Сотрудник под id {message.from_user.id} забрал {money} монет у пользователя под id {user} из группы {group} по причине "{reason}"')
                                await bot.send_message(message.chat.id,"Монеты забраны",reply_to_message_id=message.id)
                        case 3:
                            user=message.reply_to_message.from_user.id
                            group=text[1]
                            money=int(text[2])
                            minus_money(user,group,money)
                            write_log(f'Сотрудник под id {message.from_user.id} забрал {money} монет у пользователя под id {user} из группы {group}')
                            await bot.send_message(message.chat.id,"Монеты забраны",reply_to_message_id=message.id)
            case _:
                await bot.send_message(message.chat.id,"Данная команда доступна только в группе поддержки",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Выдать вип-статус",chat_types=['supergroup','group'])
    async def give_VIP(message):
        match message.chat.id:
            case _ if personal_group==message.chat.id:
                role=search_personal(message.from_user.id)
                if role==None:
                    await bot.send_message(message.chat.id,"Вы не являетесь сотрудником поддержки",reply_to_message_id=message.id)
                else:
                    text=message.text.split("  ")
                    match len(text):
                        case 4:
                            user=text[1]
                            days=int(text[2])
                            reason=text[3]
                            update_vip(user,days,True)
                            write_log(f'Сотрудник под id {message.from_user.id} выдал {days} дней вип-статуса пользователю под id {user} по причине "{reason}"')
                            await bot.send_message(message.chat.id,"Вип-статус выдан",reply_to_message_id=message.id)
                        case 3:
                            if message.reply_to_message==None:
                                user=text[1]
                                days=text[2]
                                update_vip(user,days,True)
                                write_log(f'Сотрудник под id {message.from_user.id} выдал {days} дней вип-статуса пользователю под id {user}')
                                await bot.send_message(message.chat.id,"Вип-статус выдан",reply_to_message_id=message.id)
                            else:
                                user=message.reply_to_message.from_user.id
                                days=int(text[1])
                                reason=text[2]
                                update_vip(user,days,True)
                                write_log(f'Сотрудник под id {message.from_user.id} выдал {days} дней вип-статуса пользователю под id {user} по причине "{reason}"')
                                await bot.send_message(message.chat.id,"Вип-статус выдан",reply_to_message_id=message.id)
            case _:
                await bot.send_message(message.chat.id,"Данная команда доступна только в группе поддержки",reply_to_message_id=message.id)
    @bot.message_handler(regexp="Забрать вип-статус",chat_types=['supergroup','group'])
    async def fetch_VIP(message):
        match message.chat.id:
            case _ if personal_group==message.chat.id:
                role=search_personal(message.from_user.id)
                if role==None:
                    await bot.send_message(message.chat.id,"Вы не являетесь сотрудником поддержки",reply_to_message_id=message.id)
                else:
                    text=message.text.split("  ")
                    match len(text):
                        case 4:
                            user=text[1]
                            days=int(text[2])
                            reason=text[3]
                            update_vip(user,days,False)
                            write_log(f'Сотрудник под id {message.from_user.id} забрал {days} дней вип-статуса у пользователя под id {user} по причине "{reason}"')
                            await bot.send_message(message.chat.id,"Вип-статус забран",reply_to_message_id=message.id)
                        case 3:
                            if message.reply_to_message==None:
                                user=text[1]
                                days=text[2]
                                update_vip(user,days,False)
                                write_log(f'Сотрудник под id {message.from_user.id} забрал {days} дней вип-статуса у пользователя под id {user}')
                                await bot.send_message(message.chat.id,"Вип-статус забран",reply_to_message_id=message.id)
                            else:
                                user=message.reply_to_message.from_user.id
                                days=int(text[1])
                                reason=text[2]
                                update_vip(user,days,False)
                                write_log(f'Сотрудник под id {message.from_user.id} забрал {days} дней вип-статуса у пользователя под id {user} по причине "{reason}"')
                                await bot.send_message(message.chat.id,"Вип-статус забран",reply_to_message_id=message.id)
            case _:
                await bot.send_message(message.chat.id,"Данная команда доступна только в группе поддержки",reply_to_message_id=message.id)