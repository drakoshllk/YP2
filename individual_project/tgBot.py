from math import trunc

import telebot, random, time
from telebot import types

bot = telebot.TeleBot('7215955531:AAH9xQ7vkJs_SuZRF9CWcLgbfgW7lvHsMEs')

wallet, balance = 30000, 10000
welcome_message = "Привет, лудик, в нашем казино есть несколько игр: крашер, слоты и блэкджек. Так же у тебя есть баланс казино и твой кошель. Ты можешь как вывести баланс с казика, так и пополнить. Так же ты можешь взять вирты в долг. Проверить баланс и кошелек ты можешь посмотрет по соответствующей кнопке. Приятной игры и удачи!"
slots_arr = ('🟡', '💎', '🍋', '🍏', '🍒', '7️⃣')

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = (types.KeyboardButton('Проверить кошелек'), types.KeyboardButton('Проверить баланс'), types.KeyboardButton('Взять кредит'),
                types.KeyboardButton('Вывод'), types.KeyboardButton('Додэп'), types.KeyboardButton('Крашер'),
                types.KeyboardButton('Слоты'), types.KeyboardButton('Блэкджэк'), types.KeyboardButton('Коинфлип'))
    reply_markup = types.ReplyKeyboardMarkup()
    reply_markup.row(keyboard[0], keyboard[1], keyboard[2])
    reply_markup.row(keyboard[3], keyboard[4])
    reply_markup.row(keyboard[5], keyboard[6], keyboard[7])
    reply_markup.row(keyboard[8])
    bot.send_message(message.chat.id, welcome_message, reply_markup=reply_markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Проверить кошелек':
        bot.send_message(message.chat.id, f'В твоем кошельке {wallet} виртов')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Проверить баланс':
        bot.send_message(message.chat.id, f'На твоем балансе {balance} виртов')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Взять кредит':
        debt_value = bot.send_message(message.chat.id, 'Напиши сумму кредита')
        bot.register_next_step_handler(debt_value, credit)
    elif message.text == 'Вывод':
        withdraw_value = bot.send_message(message.chat.id, 'Напиши сумму вывода')
        bot.register_next_step_handler(withdraw_value, withdraw)
    elif message.text == 'Додэп':
        dodep_value = bot.send_message(message.chat.id, 'Напиши сумму додэпчика')
        bot.register_next_step_handler(dodep_value, dodep)
    elif message.text == 'Крашер':
        usr_msg = bot.send_message(message.chat.id, 'Напиши сумму ставки и икс на который ставишь через запятую')
        bot.register_next_step_handler(usr_msg, crasher)
    elif message.text == 'Слоты':
        usr_msg = bot.send_message(message.chat.id, 'Напиши сумму ставки')
        bot.register_next_step_handler(usr_msg, slots)
    elif message.text == 'Блэкджэк':
        usr_msg = bot.send_message(message.chat.id, 'Напиши сумму ставки')
        bot.register_next_step_handler(usr_msg, blackjack)
    elif message.text == 'Коинфлип':
        usr_msg = bot.send_message(message.chat.id, 'Напиши сумму ставки')
        bot.register_next_step_handler(usr_msg, coinflip)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')
        bot.register_next_step_handler(message, on_click)


def coinflip(message):
    global bet_amount
    try:
        bet_amount = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверное число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance
    if bet_amount > balance or bet_amount < 0:
        bot.send_message(message.chat.id, 'У вас нет столько денег на счету!')
        bot.register_next_step_handler(message, on_click)
    else:
        balance -= bet_amount
        var_data = bot.send_message(message.chat.id, f'Со счета списано {bet_amount}')
        time.sleep(2)
        bot.edit_message_text("Подкидываем монетку...", var_data.chat.id, var_data.message_id)
        time.sleep(4)


def blackjack(message):
    global bet_amount
    try:
        bet_amount = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверное число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance
    if bet_amount > balance or bet_amount < 0:
        bot.send_message(message.chat.id, 'У вас нет столько денег на счету!')
        bot.register_next_step_handler(message, on_click)
    else:
        balance -= bet_amount
        var_data = bot.send_message(message.chat.id, f'Со счета списано {bet_amount}')
        time.sleep(2)
        bot.edit_message_text("Раздача...", var_data.chat.id, var_data.message_id)
        time.sleep(4)
        diler_hand = random.randint(15, 23)
        cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10)
        global player_hand
        player_hand = random.choice(cards) + random.choice(cards)
        if diler_hand > 21 and player_hand != 21:
            balance += bet_amount * 2
            bot.edit_message_text(f'Вы Выиграли! Дилер перебрал!\n'
                                  f'На ваш счет зачислено: {bet_amount * 2}', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)
        elif player_hand == 21 and diler_hand != 21:
            balance += bet_amount * 2.5
            bot.edit_message_text(f'Блэкджек! Вы Выиграли!\n'
                                  f'На ваш счет зачислено: {bet_amount * 2.5}', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)
        else:
            if player_hand_generate(player_hand, var_data):
                pass
            else:
                pass

def player_hand_generate(player_hand, var_data):

    reply_markup = types.InlineKeyboardMarkup()
    keyboard = (types.InlineKeyboardButton('Взять', callback_data='take'), types.InlineKeyboardButton('Хватит', callback_data='drop'))
    reply_markup.row(keyboard[0])
    reply_markup.row(keyboard[1])
    bot.edit_message_text(f'В вашей руке {player_hand}\n', var_data.chat.id, var_data.message_id, reply_markup=reply_markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'take':
        pass
    elif callback.data == 'drop':
        pass

def slots(message):
    global bet_amount
    try:
        bet_amount = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверное число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance
    if bet_amount > balance or bet_amount < 0:
        bot.send_message(message.chat.id, 'У вас нет столько денег на счету!')
        bot.register_next_step_handler(message, on_click)
    else:
        balance -= bet_amount
        var_data = bot.send_message(message.chat.id, f'Со счета списано {bet_amount}')
        time.sleep(2)
        global slots_arr
        play_combination = [random.choice(slots_arr), random.choice(slots_arr), random.choice(slots_arr)]
        combination_str = ""
        for i in range(3):
            combination_str += play_combination[i]
            bot.edit_message_text(combination_str, var_data.chat.id, var_data.message_id)
            time.sleep(4)
        if all(i == play_combination[0] for i in play_combination):
            win_amount = calculate_win_amount(play_combination, bet_amount)
            balance += win_amount
            bot.edit_message_text(f'Вы Выиграли!\nВаша ставка: {bet_amount}\n'
                                       f'На ваш счет зачислено: {win_amount}', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)
        else:
            bot.edit_message_text(f'Вы проиграли!', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)

def calculate_win_amount(play_combination, bet_amount):
    global slots_arr
    if play_combination[0] == slots_arr[0]:
        return bet_amount * 100
    elif play_combination[0] == slots_arr[1]:
        return bet_amount * 10
    elif play_combination[0] == slots_arr[2]:
        return bet_amount * 5
    elif play_combination[0] == slots_arr[3]:
        return bet_amount * 3
    elif play_combination[0] == slots_arr[4]:
        return bet_amount
    elif play_combination[0] == slots_arr[5]:
        return bet_amount * 1000

def crasher(message):
    global bet_amount, user_x
    try:
        bet_amount, user_x = message.text.split(',')
        bet_amount = int(bet_amount)
        user_x = round(float(user_x), 2)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверная форма ввода ставки!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance
    if bet_amount > balance or bet_amount < 0 or user_x < 0 or user_x > 10:
        bot.send_message(message.chat.id,'Либо у вас нет столько денег на счету, либо ставка недопустима!')
        bot.register_next_step_handler(message, on_click)
    else:
        balance -= bet_amount
        var_data = bot.send_message(message.chat.id, f'Со счета списано {bet_amount}')
        time.sleep(2)
        bot.edit_message_text("Так так, что тут у нас", var_data.chat.id, var_data.message_id)
        time.sleep(5)
        generated_x = round(random.uniform(1, 7), 2)
        if user_x <= generated_x:
            win_amount = round(bet_amount * user_x, 2)
            if win_amount % 1 == 0:
                win_amount = int(win_amount)
            balance += win_amount
            bot.edit_message_text(f'Вы Выиграли!\nВаша ставка: {bet_amount}\n'
                                       f'Икс на который вы поставили: {user_x}\n'
                                       f'Икс, который выпал: {generated_x}\n'
                                       f'На ваш счет зачислено: {win_amount}', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)
        else:
            bot.edit_message_text(f'Вы проиграли!\nВаша ставка: {bet_amount}\n'
                                       f'Икс на который вы поставили: {user_x}\n'
                                       f'Икс, который выпал: {generated_x}', var_data.chat.id, var_data.message_id)
            bot.register_next_step_handler(message, on_click)

def dodep(message):
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели недопустимое число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance, wallet
    if value <= wallet and value >= 0:
        balance += value
        wallet -= value
        bot.send_message(message.chat.id, 'Пополнение прошло успешно!')
        bot.register_next_step_handler(message, on_click)
    else:
        bot.send_message(message.chat.id, 'В твоем кошельке нет столько деняг!')
        bot.register_next_step_handler(message, on_click)

def withdraw(message):
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели недопустимое число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    global balance, wallet
    if value <= balance and value >= 0:
        balance -= value
        wallet += value
        bot.send_message(message.chat.id, 'Вывод прошел успешно!')
        bot.register_next_step_handler(message, on_click)
    else:
        bot.send_message(message.chat.id, 'На твоем счету в казиныче нет столько деняг!')
        bot.register_next_step_handler(message, on_click)

def credit(message):
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели недопустимое число!')
        bot.register_next_step_handler(message, on_click)
        return 1
    if value > 0:
        global wallet
        wallet += value
        bot.send_message(message.chat.id, 'Вы успешно взяли кредит!')
        bot.register_next_step_handler(message, on_click)
    else:
        bot.send_message(message.chat.id, 'Недопустимая сумма кредита')
        bot.register_next_step_handler(message, on_click)

bot.infinity_polling()