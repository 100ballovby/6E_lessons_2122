import random as r

n = r.randint(-100, 100)  # случайное число от -100 до 100

print(f'Сгенерировалось: {n}')

if n in range(1, 101):  # Если число находится в промежутке от 1 до 100
    print(n)
elif n == 0:  # иначе если число равно 0
    print('Не подходит!')
else:  # иначе (когда число меньше 0)
    print(n * -1)