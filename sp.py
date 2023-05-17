import telebot
import random
from sksksks import *

TOKEN = '5880854228:AAFPO4PGV6gOtBot3f-2H_ytqm2qs5b57Y0'

bot = telebot.TeleBot(TOKEN)

sticker_id = ["CAACAgEAAxkBAAEJAg1kZHvQyvPQ5w-qHwTqNp7lDp4Y1AACCAADhy7gGgfIUDPuHksOLwQ", "CAACAgEAAxkBAAEJAg5kZHvQVC5WXM23rvGbxwhe_9BzrQACMgADhy7gGhl0yl2desA9LwQ", "CAACAgUAAxkBAAEJAg9kZHvQao4jgtVlo6kjRG0zPvibwQACfAkAAgQlwVfMh_gCAYukfC8E", "CAACAgUAAxkBAAEJAhBkZHvQrklA4XP03Hl2CJWQNJjmLQACSQADjzX8Djv2Sj3K4SEXLwQ", "CAACAgIAAxkBAAEJAhVkZHwm62BpUws8MjhhsRxvGc8S9gACVBMAAp5IyEsxwcY2Kt_j8S8E", "CAACAgUAAxkBAAEJAhdkZHxvIB3VkSGwmRtqM-9oh6H03wACPgQAAqWDpQj-Rthefz94oy8E"]
pooja_id = ["CAACAgUAAxkBAAEJAddkZHFQfrYEiAF_iQ0JtKnWIOVSWQACBgMAAqTLyVZ2ioYdBMRkQi8E", "CAACAgUAAxkBAAEJAedkZHO39edAz2yipCQeBuLCdj7KEgACJQIAAjsl0Fbt9j1dyRcUGi8E", "CAACAgUAAxkBAAEJAelkZHVytZnZLvFraJwRBjT-vJ8y-QAC-AIAAgXV0VarHvMRSvM8XS8E", "CAACAgUAAxkBAAEJAetkZHV03SizcZW0p6UPGS34zg2P9AACTAIAAm_t0VYgSG75rDZF8y8E", "CAACAgUAAxkBAAEJAe1kZHV2GsfOa9Vmr7nB8J0-6TtRCwAC9gMAAv-yyVb9jffZur5dLS8E", "CAACAgUAAxkBAAEJAe9kZHV37v_OT-QHb-S340e8OYMB4wAC_wIAAiiiyVYq1ox14XU9si8E", "CAACAgUAAxkBAAEJAfFkZHV5mDAUoWS6WL5HTYeOll2-vQACFQIAAi4vyVaVIYoHAAF17nEvBA", "CAACAgUAAxkBAAEJAfNkZHV6FDIEi0AhNIOxfiuVNuHRVwAC4wIAAsgyyFbVypKGfSgyOC8E", "CAACAgUAAxkBAAEJAfVkZHWxtAXjGcZELBG_amAUVF9gBAAC6QIAAoPCyFbE4lKLIxHx1y8E", "CAACAgUAAxkBAAEJAfZkZHWze4Jli8eSdNHxLy7dw-C6AQACNQMAAvkfyVa-OWL_3AiRcC8E", "CAACAgUAAxkBAAEJAflkZHW17FLmhhLk88Pg9Le8d4GnjwACagIAAtdRyVbizWsufVPj0i8E", "CAACAgUAAxkBAAEJAftkZHW3wPmsSb3Kt-VakQABOUysvt8AAmsBAAIG38lWyXOaVQ36MhIvBA", "CAACAgUAAxkBAAEJAf1kZHW5v8IMEUa8eUk3DkODUJwGNQACvgEAAgjeyFb5AAGoRSXF8TwvBA", "CAACAgUAAxkBAAEJAf5kZHW59xOUcO6GBdrvgGodtx18iAACewIAAroB0VYedEPdXzugGy8E", "CAACAgUAAxkBAAEJAgFkZHW7o-JCNzEIBOMKPKVhMQY0iwAC5AIAAtgQ0VbBYdkI715mLS8E", "CAACAgUAAxkBAAEJAgJkZHW8J8eFFwfGTlHDEMK0eejxJQAC7wIAAgpdyFaKU-H5Yfl8Ry8E", "CAACAgUAAxkBAAEJAgRkZHW91rCMyKxjEcu4xiJhhuWMUAAC8wEAAry9yFb6FA-xg-ozIy8E", "CAACAgUAAxkBAAEJAgVkZHW9R85h4mgTKHlgm17vBiaT-AACxwIAAp_S0VaoPZU4dIipGS8E", "CAACAgUAAxkBAAEJAgdkZHW-ThtMDS4P74K427HygYrYrgACOgIAAuAUyVZna2KkVUHQgy8E"]
inputs_m = {}
inputs_f = {}
outputs_m = {}
outputs_f = {}
count = {}

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    global inputs_m, inputs_f, count
    user_id = message.chat.id
    inputs_m[user_id] = {"M1":[],"M2":[],"M3":[],"M4":[],"M5":[],"M6":[]}
    inputs_f[user_id] = {"F1":[],"F2":[],"F3":[],"F4":[],"F5":[],"F6":[]}
    outputs_m[user_id] = {"M1":[],"M2":[],"M3":[],"M4":[],"M5":[],"M6":[]}
    outputs_f[user_id] = {"F1":[],"F2":[],"F3":[],"F4":[],"F5":[],"F6":[]}
    count[user_id] = 1
    instructions(message)
    prompt(message)
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Please do /instructions if you are unsure how to use the bot\n\nPlease do /result for the pairing results to be repeated\n\nIf you have any misinputs, please type /restart to start from the beginning")

@bot.message_handler(commands=['instructions'])
def instructions(message):
    bot.send_message(message.chat.id, "Please input the rankings of M1 - M6 for F1 - F6 and vice versa\n\nFor each of the inputs, please input the rankings separated by a comma, 6 being most preferred and 1 being least. e.g. 5,6,3,2,1,4\n\nMake sure to check that the rankings given to you have one of each number from 1 - 6 (i.e. there should be NO duplicates)\n\nif there are less than 12 people (e.g. missing one male and one female), their entries should be 0,0,0,0,0,0 AND when people rank them in their ranking sheet, it should be 0 (e.g. there is no M6 and F6, so ranking slip could look like this: 2,3,4,5,6,0)\n\n Please do /help for other commands or contact @p0ngster or @meganyeo for assistance")

@bot.message_handler(commands=['result'])
def result(message):
    global inputs_m, inputs_f, outputs_m, outputs_f
    user_id = message.chat.id
    for key in inputs_m[user_id]:
        if len(inputs_m[user_id][key]) == 0:
            bot.send_message(message.chat.id, "bitch wtf there are no stored input values dumbfk")
            return prompt(message)
        outputs_m[user_id][key] = [int(i) for i in inputs_m[user_id][key]]
    for key in inputs_f[user_id]:
        if len(inputs_f[user_id][key]) == 0:
            bot.send_message(message.chat.id, "bitch wtf there are no stored input values dumbfk")
            return prompt(message)
        outputs_f[user_id][key] = [int(i) for i in inputs_f[user_id][key]]       
    groups = split_into_groups(outputs_m[user_id], outputs_f[user_id])
    bot.send_message(message.chat.id, f"The pairings are as follows:\n\n{groups[0][0]} {groups[0][1]}\n{groups[1][0]} {groups[1][1]}\n{groups[2][0]} {groups[2][1]}\n{groups[3][0]} {groups[3][1]}\n{groups[4][0]} {groups[4][1]}\n{groups[5][0]} {groups[5][1]}\n\nRefer to the above and pair up the freshies from the top to bottom pairings, ignore the respective pairings if freshie is not participating.\n\nWhen splitting them into their respective rooms, try to make it as even as possible (e.g. if all 6 pairs are present, put first 3 pairs into one room, and the last 3 pairs into the other room.\n\nIf there are 5 pairs, put the first 3 pairs in one room, 4th and 5th pair in the other room) pairings are important as this will be the first pairing that will be used for the first game that is played together.")

def prompt(message):
    global count
    user_id = message.chat.id
    if 1 <= count[user_id] <= 6:
        bot.send_message(message.chat.id, f"Please enter M{count[user_id]}'s rankings of F1-F6")
    elif 7 <= count[user_id] <= 12:
        bot.send_message(message.chat.id, f"Please enter F{count[user_id] - 6}'s rankings of M1-M6")
    else:
        count[user_id] = 0
        result(message)

def finished(message):
    bot.send_message(message.chat.id, "All ranking strips have been submitted, if you would like a repeat of the result, please do /result.\n\nIf there was an error in the inputs, please do /restart and start from the beginning.")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    photo_id = "https://media.npr.org/assets/img/2017/09/12/macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s1100-c50.jpg"
    return bot.send_photo(message.chat.id, photo_id)

@bot.message_handler(commands=['pooja'])
def pooja(message):
    global pooja_id
    return bot.send_sticker(message.chat.id, random.choice(pooja_id))

@bot.message_handler(commands=['dontpressthis'])
def dontpressthis(message):
    return bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEJAiVkZH4bGC3m-bfQ2lVHqIwjh-odowACnREAAg3s0UtQX20y8kWzLi8E")

@bot.message_handler(content_types=['sticker'])           
def handle_sticker(message):
    global sticker_id
    # for d in range (len(sticker_id)):
    #     bot.send_sticker(message.chat.id, sticker_id[d])
    return bot.send_sticker(message.chat.id, random.choice(sticker_id))

@bot.message_handler(func=lambda message: True)
def handle_input(message):
    global inputs_m, inputs_f, count
    user_id = message.chat.id
    try:
        if user_id not in inputs_m:
            return start(message)
        input_list = message.text.split(',')
        if len(input_list) != 6:
            raise ValueError
        input_set = set(input_list)
        # if (len(input_set) != 6):
        #     raise ValueError
        for num in input_set:
            if not num.isnumeric() or int(num) < 0 or int(num) > 6:
                raise ValueError             
        if count[user_id] == 0:
            print(count)
            finished(message)
        elif  0 < count[user_id] < 7:
            name = "M" + str(count[user_id])
            inputs_m[user_id][name] = (input_list)
            count[user_id] += 1
            print(inputs_m)
            print(count)
            prompt(message)
        else:
            name = "F" + str(count[user_id] - 6)
            inputs_f[user_id][name] = (input_list)
            count[user_id] += 1
            print(inputs_f)
            print(count)
            prompt(message)
    except ValueError:
        if count[user_id] == 0:
            return finished(message)
        else:
            bot.send_message(message.chat.id, "Invalid input. Please enter 6 unique digits separated by commas e.g. 5,6,3,2,1,4. Ranking score should not exceed 6.\n\nPlease do /restart if you made a mistake with the inputs or are unsure of how to input the rankings.")
            prompt(message)
    
bot.polling()
