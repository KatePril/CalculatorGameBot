from random import randint
from aiogram import types

def generate_number():
    return randint(0, 100)

def generate_expression():
    actions = ['-', '+', '*', '/']
    return f'{generate_number()} {actions[randint(0, 3)]} {generate_number()}'

def generate_result(correct_answer):
    tmp = randint(0, 1000)
    while True:
        if tmp != correct_answer:
            return tmp
        else:
            tmp = randint(0, 1000)

def give_question():
    expression = generate_expression()
    correct_answer = randint(0, 3)
    correct_result = eval(expression)
    markup = types.InlineKeyboardMarkup()
    
    for i in range(4):
        if i == correct_answer:
            markup.add(types.InlineKeyboardButton(correct_result, callback_data='correct_answer'))
        else:
            markup.add(types.InlineKeyboardButton(generate_result(correct_result), callback_data='wrong_answer'))
            
    return expression, markup