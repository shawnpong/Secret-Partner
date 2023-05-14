import telebot
from sksksks import *

TOKEN = '5880854228:AAFPO4PGV6gOtBot3f-2H_ytqm2qs5b57Y0'

bot = telebot.TeleBot(TOKEN)

inputs_m = {}
inputs_f = {}
count = 1

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    global inputs_m, inputs_f, count
    inputs_m = {}
    inputs_f = {}
    count = 1
    bot.send_message(message.chat.id, "For each of the inputs, please input the rankings separated by a comma, 1 being most preferred and 6 being least. e.g. 5,6,3,2,1,4\n\nIf you have any misinputs, please type /restart to start from the beginning or /help for other commands.")
    prompt(message)
    

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start or /restart if you made a mistake with the inputs\n\n/result for the pairing results to be repeated")

@bot.message_handler(commands=['result'])
def result(message):
    global inputs_m, inputs_f
    group_a, group_b = split_into_groups(inputs_m.values(), inputs_f.values())
    room_1 = "\n".join([f"{f} {m}" for f, m in zip(group_a, group_b)])
    room_2 = "\n".join([f"{f} {m}" for f, m in zip(group_b, group_a)])
    bot.send_message(message.chat.id, f"The pairings are as follows:\n\nRoom 1\n\n{room_1}\n\nRoom 2\n\n{room_2}")

def prompt(message):
    global count
    user_id = message.from_user.id
    if 1 <= count <= 6:
        bot.send_message(message.chat.id, f"Please enter your rankings of F1-F6")
    elif 7 <= count <= 12:
        bot.send_message(message.chat.id, f"Please enter your rankings of M1-M6")
    else:
        result(message)
        return
    count += 1
            

@bot.message_handler(func=lambda message: True)
def handle_input(message):
    global inputs_m, inputs_f
    try:
        input_list = message.text.split(',')
        if len(input_list) != 6:
            raise ValueError
        input_set = set(input_list)
        if len(input_set) != 6:
            raise ValueError
        for num in input_set:
            if not num.isnumeric() or int(num) < 1 or int(num) > 6:
                raise ValueError
        
        user_id = message.from_user.id
        if  0 < count < 7:
            inputs_f[user_id] = input_list
        elif 7 <= count <= 12:
            inputs_m[user_id] = input_list
        
        prompt(message)
            
    except ValueError:
        bot.send_message(message.chat.id, "Invalid input. Please enter 6 unique digits separated by commas e.g. 5,6,3,2,1,4")

bot.polling()