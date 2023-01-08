from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from config_reader import config

import asyncio

import requests

bot = Bot(token=config.bot_token.get_secret_value())

# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        'Aloha👋 I\'m a bot that helps you not be bored 🥱😞 and have fun answering your friends instead of simple "Yes" or "No" 😂')
    kb = [
        [types.KeyboardButton(text="Yes")],
        [types.KeyboardButton(text="No")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Yes or no? That is the question🤔")

    await message.answer("Press the buttons and smile😋", reply_markup=keyboard)


@dp.message_handler(Text(equals=["Да", "да", "Yes", "yes"]))
async def cmd_yes(message: types.Message):
    await message.answer_animation(get_gif('yes'))


@dp.message_handler(Text(equals=["Нет", "нет", 'No', 'no']))
async def cmd_no(message: types.Message):
    await message.answer_animation(get_gif('no'))


@dp.message_handler(Text(equals=["net", "Net"]))
async def cmd_net(message: types.Message):
    await message.reply('Pi*ora otvet😜')


@dp.message_handler(Text(equals=["da", "Da"]))
async def cmd_da(message: types.Message):
    await message.reply('Do you want me to answer in rhyme?😜')


@dp.message_handler(Text(equals=["maybe"]))
async def cmd_maybe(message: types.Message):
    await message.answer_animation(get_gif('maybe'))


@dp.message_handler()
async def cmd_cant_do_this(message: types.Message):
    if message.from_id == 673711809:
        await message.reply('Slava, is that you?🤨 Don\'t waste my time😉')
    else:
        await message.reply('Sorry! I don\'t understand it😞')


def get_gif(answer):
    params = dict(force=answer)
    response = requests.get(config.api_site, params)
    response_json = response.json()

    return response_json['image']

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
