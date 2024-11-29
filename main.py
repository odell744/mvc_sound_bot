#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('6877401963:AAEUvgxo_UxtTsYdWWE40H3SwxAJCwB0NYY')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


def main():
    asyncio.run(bot.polling())


if __name__ == "__main__": # зачем __name__ https://habr.com/ru/articles/702218/
    main()