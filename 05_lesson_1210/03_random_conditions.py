"""Написать программу, которая будет помогать
пользователю принять решение. То есть: пользователь
должен задать программе вопрос, а она должна ответить:
да, нет или наверное"""
import random as r

question = input('Задай свой вопрос: ')
answer = r.randint(1, 3)  # 1 до 3, потому что 3 ответа

if answer == 1:  # если сгенерировалось число 1, то:
    print('Да!')  # написать "Да!"
elif answer == 2:  # иначе если сгенерировалось число 2, то:
    print('Нет!')  # написать "Нет!"
else:  # иначе (если сгенерировалось число 3)
    print('Наверное...')  # написать "Наверное"


