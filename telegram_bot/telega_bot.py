# import telebot
# from MyToken import token
# from telebot import types

# bot = telebot.TeleBot(token)

# entry = {}

# inline_keyboard = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton('Доход', callback_data = 'income')
# btn2 = types.InlineKeyboardButton('Расход', callback_data = 'costs')
# inline_keyboard.add(btn1, btn2)


# @bot.callback_query_handler(func=lambda c: True)
# def inline(c):
#     if c.data == 'income':
#         chat_id = c.message.chat.id
#         income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
#         k1 = types.KeyboardButton('Работа')
#         k2 = types.KeyboardButton('Фриланс')
#         k3 = types.KeyboardButton('Другое')
#         income_keyboard.add(k1, k2, k3)
#         msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup = income_keyboard)
#         bot.register_next_step_handler(msg, get_category_income)


#     if c.data == 'costs':
#         chat_id = c.message.chat.id
#         costs_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
#         k1 = types.KeyboardButton('Еда')
#         k2 = types.KeyboardButton('Одежда')
#         k3 = types.KeyboardButton('Развлечения')
#         costs_keyboard.add(k1, k2, k3)
#         msg = bot.send_message(chat_id, 'Выберите категорию', reply_markup = costs_keyboard)
#         bot.register_next_step_handler(msg, get_category_costs)


# def get_category_income(message):
#     chat_id = message.chat.id
#     entry.update({'category': message.text})
#     msg = bot.send_message(chat_id, 'Enter the amount')
#     bot.register_next_step_handler(msg, get_sum_income)

# def get_sum_income(message):
#     chat_id = message.chat.id
#     entry.update({'sum': message.text})

#     file_name = 'income.csv'
#     with open(file_name, 'a', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow( (entry['category'], entry['sum']) )

#     bot.send_message(chat_id, 'Your income is added', reply_markup = inline_keyboard)
#     bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEDuf1h6s2FAZ4WMlfKrY-20Q5-6zxbBwAC3gADe-lQG0dpoSHKmm-jIwQ')


# def get_category_costs(message):
#     chat_id = message.chat.id
#     entry.update({'category': message.text})
#     msg = bot.send_message(chat_id, 'Enter the amount')
#     bot.register_next_step_handler(msg, get_sum_costs)

# def get_sum_costs(message):
#     chat_id = message.chat.id
#     entry.update({'sum': message.text})

#     file_name = 'costs.csv'
#     with open(file_name, 'a', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow( (entry['category'], entry['sum']) )

#     bot.send_message(chat_id, 'Your costs are added', reply_markup = inline_keyboard)
#     bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEDuf1h6s2FAZ4WMlfKrY-20Q5-6zxbBwAC3gADe-lQG0dpoSHKmm-jIwQ')





# # def start_message(message):
# #     # print(message)
# #     chat_id = message.chat.id
# #     print(chat_id)
# #     bot.send_message(chat_id, "Hello! I'm python_test bot.")

# # @bot.message_handler(content_types=['sticker', 'text'])
# # def send_sticker(message):
# #     chat_id = message.chat.id
# #     if message.text.lower() == 'hello':
# #         bot.send_message(chat_id, 'Hello, my dear!')
# #     bot.send_sticker(chat_id, 'CAACAgQAAxkBAAEDvSRh7aWZ7Eez1AH5lhGk0gHDLdRZJgAChggAApczAAFT0H2bWSavuLAjBA')

# bot.polling()
