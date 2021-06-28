from django.shortcuts import render
import telegram

token = '***'
my_id = ****
egor_id = ***
olga_id = ***
telegramBot = telegram.Bot(token)

def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")
    # telegramBot.sendMessage(olga_id, text, parse_mode="Markdown")
    # telegramBot.sendMessage(egor_id, text, parse_mode="Markdown")
