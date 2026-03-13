import asyncio
from datetime import datetime, timedelta

from telebot import types
from boot import *

admins_chat = ""
bot_message_test: int = None
answer = 0
loop = False


def coms(bot):
    @bot.message_handler(commands=["Start"], chat_types=["private"])
    async def start(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(
            text="Наш сайт", url="https://wolfbot.ru"
        )
        markup.add(btn1)

        await bot.send_message(
            message.chat.id,
            f"Помощь по работе бота wolfbot.\nТехническая поддержка:\n{sup}",
            reply_markup=markup,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )

    @bot.message_handler(
        regexp="Админы|Admins", chat_types=["supergroup", "group"]
    )
    async def admins(message):
        global admins_chat

        info = await bot.get_chat_administrators(message.chat.id)
        for i in info:
            admins_chat = (
                admins_chat
                + f"[{i.user.first_name}](https://t.me/{i.user.username})\n"
            )

        await bot.send_message(
            message.chat.id,
            f"Список администраторов:\n{admins_chat}",
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )

    @bot.message_handler(regexp="[Rr]eg|[Рр]ег")
    async def mes(message):
        check = search_filter(
            message.from_user.id, message.from_user.username
        )

    @bot.message_handler(content_types=["new_chat_members"])
    async def nu(message):
        check = search_filter(
            message.from_user.id, message.from_user.username
        )
        if not check:
            global time_test, bot_message_test, answer
            await bot.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                can_send_messages=False,
            )
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(
                text="Да", callback_data="Ответ_Да"
            )
            btn2 = types.InlineKeyboardButton(
                text="Нет", callback_data="Ответ_Нет"
            )
            markup.add(btn1, btn2)
            mes_test = await bot.send_message(
                message.chat.id,
                f"@{message.from_user.username}, Ты атеист? На ответ две минуты",
                reply_markup=markup,
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
            time_test = datetime.now() + timedelta(minutes=2)
            bot_message_test = int(mes_test.message_id)

            while datetime.now() < time_test and answer == 0:

                @bot.callback_query_handler(
                    lambda call: call.data.startswith("Ответ_")
                )
                async def handle_callback(call):
                    global bot_message_test, time_test, answer
                    await bot.answer_callback_query(call.id)
                    if (
                        call.data == "Ответ_Да"
                        or call.data == "Ответ_Нет"
                    ):
                        answer = 1
                        await bot.restrict_chat_member(
                            message.chat.id,
                            message.from_user.id,
                            can_send_messages=True,
                        )
                        await bot.delete_message(
                            message.chat.id, bot_message_test
                        )
                        bot_message_test = None
                        time_test = None

                await asyncio.sleep(10)

            if answer == 0:
                await bot.delete_message(
                    message.chat.id, bot_message_test
                )
                await bot.kick_chat_member(
                    message.chat.id, message.from_user.id
                )
                bot_message_test = None
                time_test = None
            else:
                answer = 0
        else:
            await bot.ban_chat_member(
                message.chat.id, message.from_user.id
            )
            await bot.delete_message(message.chat.id, message.id)

    @bot.message_handler(chat_types=["supergroup", "group"])
    async def mes(message):
        print(message)
