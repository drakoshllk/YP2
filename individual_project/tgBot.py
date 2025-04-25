import telebot, random, time
from telebot import types

bot = telebot.TeleBot('7215955531:AAH9xQ7vkJs_SuZRF9CWcLgbfgW7lvHsMEs')

wallet, balance = 30000, 10000
welcome_message = "Привет, лудик, в нашем казино есть несколько игр: крашер, слоты и коинфлип. Так же у тебя есть баланс казино и твой кошель. Ты можешь как вывести баланс с казика, так и пополнить. Так же ты можешь взять вирты в долг. Проверить баланс и кошелек ты можешь посмотрет по соответствующей кнопке. Приятной игры и удачи!" #!ОТРЕДАКТИРОВАТЬ!

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = (types.KeyboardButton('Проверить кошелек'), types.KeyboardButton('Проверить баланс'), types.KeyboardButton('Взять кредит'),
                types.KeyboardButton('Вывод с баланса'), types.KeyboardButton('Пополнить баланс'), types.KeyboardButton('Крашер'),
                types.KeyboardButton('Однорукий бандит'), types.KeyboardButton('Коинфлип'))
    reply_markup = types.ReplyKeyboardMarkup()
    reply_markup.row(keyboard[0], keyboard[1], keyboard[2])
    reply_markup.row(keyboard[3], keyboard[4])
    reply_markup.row(keyboard[5], keyboard[6], keyboard[7])
    bot.send_message(message.chat.id, welcome_message, reply_markup=reply_markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Проверить кошелек':
        bot.send_message(message.chat.id, f'В твоем кошельке {wallet} виртов')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Проверить баланс':
        bot.send_message(message.chat.id, f'На твоем балансе {balance} виртов')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Взять кредит':
        loan_amount = bot.send_message(message.chat.id, 'Напиши сумму кредита')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(loan_amount, take_out_loan)
    elif message.text == 'Вывод с баланса':
        withdraw_value = bot.send_message(message.chat.id, 'Напиши сумму вывода')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(withdraw_value, withdraw)
    elif message.text == 'Пополнить баланс':
        replenishment_value = bot.send_message(message.chat.id, 'Напиши сумму пополнения баланса')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(replenishment_value, balance_replenishment)
    elif message.text == 'Крашер':
        user_bet = bot.send_message(message.chat.id, 'Напиши сумму ставки и икс на который ставишь через запятую')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(user_bet, crasher_game)
    elif message.text == 'Однорукий бандит':
        user_bet = bot.send_message(message.chat.id, 'Напиши сумму ставки')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(user_bet, slots_game)
    elif message.text == 'Коинфлип':
        user_bet = bot.send_message(message.chat.id, 'Напиши сумму ставки и сторону на которую ставишь через запятую (0 - решка, 1 - орел)')#!ОТРЕДАКТИРОВАТЬ!
        bot.register_next_step_handler(user_bet, coinflip_game)

def send_exit_message(message, exit_message):
    bot.send_message(message.chat.id, exit_message)
    bot.register_next_step_handler(message, on_click)

def edit_exit_message(message, message_data, exit_message):
    bot.edit_message_text(exit_message, message_data.chat.id, message_data.message_id)
    bot.register_next_step_handler(message, on_click)

def coinflip_game(message):
    try:
        user_bet, user_side = map(int, message.text.split(','))
    except ValueError:
        send_exit_message(message, 'Неверная форма ввода!')#!ОТРЕДАКТИРОВАТЬ! проверка правильности формы ввода(ставка, сторона монеты(1 или 0))
        return 1
    global balance
    if user_bet > balance:
        send_exit_message(message, 'У вас нет столько денег на счету в казино!')#!ОТРЕДАКТИРОВАТЬ!
    elif user_bet <= 0:
        send_exit_message(message, 'Недопустимая ставка!')#!ОТРЕДАКТИРОВАТЬ!
    elif user_side > 1 or user_side < 0:
        send_exit_message(message, 'Неверная форма ввода стороны монеты!')#!ОТРЕДАКТИРОВАТЬ!
    else:
        balance -= user_bet
        message_data = bot.send_message(message.chat.id, f'Со счета списано {user_bet}')
        time.sleep(2)
        bot.edit_message_text("Подкидываем монетку...", message_data.chat.id, message_data.message_id)
        time.sleep(3)
        winning_side = random.randint(0, 1)
        if winning_side == user_side:
            money_won = user_bet * 2
            balance += money_won
            edit_exit_message(message, message_data, f'Вы Выиграли!\nНа ваш счет казино зачислено: {money_won}')#!ОТРЕДАКТИРОВАТЬ!
        else:
            edit_exit_message(message, message_data, 'Вы проиграли!')#!ОТРЕДАКТИРОВАТЬ!

slots = ('🟡', '💎', '🍋', '🍏', '🍒', '7️⃣')
def slots_game(message):
    try:
        user_bet = int(message.text)
    except ValueError:
        send_exit_message(message, 'Неверное число!')#!ОТРЕДАКТИРОВАТЬ! проверка введено ли число или строка.
        return 1
    global balance
    if user_bet > balance:
        send_exit_message(message, 'У вас нет столько денег на счету в казино!')#!ОТРЕДАКТИРОВАТЬ!
    elif user_bet <= 0:
        send_exit_message(message, 'Недопустимая ставка!')#!ОТРЕДАКТИРОВАТЬ!
    else:
        balance -= user_bet
        message_data = bot.send_message(message.chat.id, f'Со счета списано {user_bet}')
        time.sleep(2)
        slot_combination, slot_combination_str = (random.choice(slots), random.choice(slots), random.choice(slots)), ''
        for i in range(3):
            slot_combination_str += slot_combination[i]
            bot.edit_message_text(slot_combination_str, message_data.chat.id, message_data.message_id)
            time.sleep(3)
        if all(slot == slot_combination[0] for slot in slot_combination):
            money_won = calculate_money_won(slot_combination, user_bet)
            balance += money_won
            edit_exit_message(message, message_data, f'Вы Выиграли!\nНа ваш счет казино зачислено: {money_won}')#!ОТРЕДАКТИРОВАТЬ!
        else:
            edit_exit_message(message, message_data, 'Вы проиграли!')#!ОТРЕДАКТИРОВАТЬ!

def calculate_money_won(slot_combination, user_bet):
    if slot_combination[0] == slots[0]:
        return user_bet * 100
    elif slot_combination[0] == slots[1]:
        return user_bet * 10
    elif slot_combination[0] == slots[2]:
        return user_bet * 5
    elif slot_combination[0] == slots[3]:
        return user_bet * 3
    elif slot_combination[0] == slots[4]:
        return user_bet
    elif slot_combination[0] == slots[5]:
        return user_bet * 1000

def crasher_game(message):
    try:
        user_bet, user_bet_X = message.text.split(',')
        user_bet = int(user_bet)
        user_bet_X = round(float(user_bet_X), 2)
    except ValueError:
        send_exit_message(message, 'Неверная форма ввода ставки!')#!ОТРЕДАКТИРОВАТЬ! форма ввода ставки(ставка, ставка на Х)
        return 1
    global balance
    if user_bet > balance:
        send_exit_message(message, 'У вас нет столько денег на счету в казино!')#!ОТРЕДАКТИРОВАТЬ!
    elif user_bet < 0 or user_bet_X < 0 or user_bet_X > 10:
        send_exit_message(message, 'Недопустимая ставка!')#!ОТРЕДАКТИРОВАТЬ! крашер работает от 1х до 10х
    else:
        balance -= user_bet
        message_data = bot.send_message(message.chat.id, f'Со счета списано {user_bet}')#!ОТРЕДАКТИРОВАТЬ!
        time.sleep(2)
        bot.edit_message_text("Летит самолетик...", message_data.chat.id, message_data.message_id)#!ОТРЕДАКТИРОВАТЬ!
        time.sleep(5)
        winning_X = round(random.uniform(1, 7), 2)
        if user_bet_X <= winning_X:
            money_won = round(user_bet * user_bet_X, 2)
            if money_won % 1 == 0:
                money_won = int(money_won)
            balance += money_won
            edit_exit_message(message, message_data, f'Вы Выиграли!\nИкс на который вы поставили: {user_bet_X}\nИкс, который выпал: {winning_X}\nНа ваш счет зачислено: {money_won}')#!ОТРЕДАКТИРОВАТЬ!
        else:
            edit_exit_message(message, message_data, f'Вы проиграли!\nИкс на который вы поставили: {user_bet_X}\nИкс, который выпал: {winning_X}')#!ОТРЕДАКТИРОВАТЬ!

def balance_replenishment(message): #пополнение баланса казика
    try:
        replenishment_value = int(message.text)
    except ValueError:
        send_exit_message(message, 'Вы ввели недопустимое число!')#!ОТРЕДАКТИРОВАТЬ! проверка является ли числом
        return 1
    global balance, wallet
    if wallet >= replenishment_value:
        balance += replenishment_value
        wallet -= replenishment_value
        send_exit_message(message, 'Пополнение прошло успешно!')#!ОТРЕДАКТИРОВАТЬ!
    elif replenishment_value <= 0:
        send_exit_message(message, 'Введено недопустимое число')#!ОТРЕДАКТИРОВАТЬ!
    else:
        send_exit_message(message, 'В твоем кошельке нет столько деняг!')#!ОТРЕДАКТИРОВАТЬ!

def withdraw(message):
    try:
        withdraw_value = int(message.text)
    except ValueError:
        send_exit_message(message, 'Вы ввели недопустимое число!')#!ОТРЕДАКТИРОВАТЬ! проверка является ли числом
        return 1
    global balance, wallet
    if balance >= withdraw_value:
        balance -= withdraw_value
        wallet += withdraw_value
        send_exit_message(message, 'Вывод прошел успешно!')#!ОТРЕДАКТИРОВАТЬ!
    elif withdraw_value <= 0:
        send_exit_message(message, 'Вы ввели недопустимое число!')#!ОТРЕДАКТИРОВАТЬ!
    else:
        send_exit_message(message, 'На твоем счету в казиныче нет столько деняг!')#!ОТРЕДАКТИРОВАТЬ!

def take_out_loan(message):
    try:
        loan_amount = int(message.text)
    except ValueError:
        send_exit_message(message, 'Вы ввели недопустимое число!')#!ОТРЕДАКТИРОВАТЬ! проверка является ли числом
        return 1
    if loan_amount > 0:
        global wallet
        wallet += loan_amount
        send_exit_message(message, 'Вы успешно взяли кредит!')#!ОТРЕДАКТИРОВАТЬ!
    else:
        send_exit_message(message, 'Недопустимая сумма кредита')#!ОТРЕДАКТИРОВАТЬ!
bot.infinity_polling()