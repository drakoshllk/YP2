import telebot
from telebot import types

bot = telebot.TeleBot('7215955531:AAH9xQ7vkJs_SuZRF9CWcLgbfgW7lvHsMEs')

# 0 - проверить кошелек, 1 - проверить баланс, 2 - взять долг, 3 - вывод бабла, 4 - додэп, 5 - крашер, 6 - слоты, 7 - блэкджек
keyboard = (types.KeyboardButton('Проверить кошелек'), types.KeyboardButton('Проверить баланс'),
           types.KeyboardButton('Взять долг'), types.KeyboardButton('Вывод'),
           types.KeyboardButton('Додэп'), types.KeyboardButton('Крашер'),
           types.KeyboardButton('Слоты'), types.KeyboardButton('Блэкджэк'))
reply_markup = types.ReplyKeyboardMarkup()
reply_markup.row(keyboard[0], keyboard[1], keyboard[2])
reply_markup.row(keyboard[3], keyboard[4])
reply_markup.row(keyboard[5], keyboard[6], keyboard[7])

wallet, balance = 30000, 10000
welcome_message = "Привет, лудик, в нашем казино есть несколько игр: крашер, слоты и блэкджек. Так же у тебя есть баланс казино и твой кошель. Ты можешь как вывести баланс с казика, так и пополнить. Так же ты можешь взять вирты в долг. Проверить баланс и кошелек ты можешь посмотрет по соответствующей кнопке. Приятной игры и удачи!"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, welcome_message, reply_markup=reply_markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Проверить кошелек':
        bot.send_message(message.chat.id, f'В твоем кошельке {wallet} виртов')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Проверить баланс':
        bot.send_message(message.chat.id, f'На твоем балансе {balance} виртов')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Взять долг':
        debt_value = bot.send_message(message.chat.id, 'Напиши сумму долга')
        bot.register_next_step_handler(debt_value, debt)
    elif message.text == 'Вывод':
        withdraw_value = bot.send_message(message.chat.id, 'Напиши сумму вывода')
        bot.register_next_step_handler(withdraw_value, withdraw)
    elif message.text == 'Додэп':
        dodep_value = bot.send_message(message.chat.id, 'Напиши сумму додэпчика')
        bot.register_next_step_handler(dodep_value, dodep)
    elif message.text == 'Крашер':
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Слоты':
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Блэкджэк':
        bot.register_next_step_handler(message, on_click)

def dodep(message):
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели недопустимое число!')
        bot.register_next_step_handler(message, on_click)
    global balance, wallet
    if value <= wallet and value > 0:
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
    global balance, wallet
    if value <= balance and value > 0:
        balance -= value
        wallet += value
        bot.send_message(message.chat.id, 'Вывод прошел успешно!')
        bot.register_next_step_handler(message, on_click)
    else:
        bot.send_message(message.chat.id, 'На твоем счету в казиныче нет столько деняг!')
        bot.register_next_step_handler(message, on_click)

def debt(message):
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели недопустимое число!')
        bot.register_next_step_handler(message, on_click)
    global wallet
    wallet += value
    bot.send_message(message.chat.id, 'Вы успешно взяли долг!')
    bot.register_next_step_handler(message, on_click)

bot.infinity_polling()