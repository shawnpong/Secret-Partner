import telebot
from sksksks import *

TOKEN = '5880854228:AAFPO4PGV6gOtBot3f-2H_ytqm2qs5b57Y0'

bot = telebot.TeleBot(TOKEN)

inputs_m = {"M1":[],"M2":[],"M3":[],"M4":[],"M5":[],"M6":[]}
inputs_f = {"F1":[],"F2":[],"F3":[],"F4":[],"F5":[],"F6":[]}
count = 1

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    global inputs_m, inputs_f, count
    inputs_m = {"M1":[],"M2":[],"M3":[],"M4":[],"M5":[],"M6":[]}
    inputs_f = {"F1":[],"F2":[],"F3":[],"F4":[],"F5":[],"F6":[]}
    count = 1
    bot.send_message(message.chat.id, "For each of the inputs, please input the rankings separated by a comma, 1 being most preferred and 6 being least. e.g. 5,6,3,2,1,4\n\nIf you have any misinputs, please type /restart to start from the beginning or /help for other commands.")
    prompt(message)
    

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start or /restart if you made a mistake with the inputs\n\n/result for the pairing results to be repeated")

@bot.message_handler(commands=['result'])
def result(message):
    for key in inputs_m:
        inputs_m[key] = [int(i) for i in inputs_m[key]]
    for key in inputs_f:
        inputs_f[key] = [int(i) for i in inputs_f[key]]
        
    (group_a, group_b) = split_into_groups(inputs_m, inputs_f)
    bot.send_message(message.chat.id, f"The pairings are as follows:\n\nRoom 1\n\n{group_a[3]} {group_a[0]}\n{group_a[4]} {group_a[1]}\n{group_a[5]} {group_a[2]}\n\nRoom 2\n\n{group_b[3]} {group_b[0]}\n{group_b[4]} {group_b[1]}\n{group_b[5]} {group_b[2]}")

def prompt(message):
    if 1 <= count <= 6:
        bot.send_message(message.chat.id, f"Please enter M{count}'s rankings of F1-F6")
    elif 7 <= count <= 12:
        bot.send_message(message.chat.id, f"Please enter F{count - 6}'s rankings of M1-M6")
    else:
        result(message)
            

@bot.message_handler(func=lambda message: True)
def handle_input(message):
    global inputs_m, inputs_f, count
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
        
            
        if  0 < count < 7:
            name = "M" + str(count)
            inputs_m[name] = (input_list)
            count += 1
            prompt(message)
            print(inputs_m)
            
        elif 7 <= count <= 12:
            name = "F" + str(count - 6)
            inputs_f[name] = (input_list)
            count += 1
            prompt(message)
            print(inputs_f)

    except ValueError:
        bot.send_message(message.chat.id, "Invalid input. Please enter 6 unique digits separated by commas e.g. 5,6,3,2,1,4")

bot.polling()
