students = [
    'Zakhar', 'Egor',
    'Simeon', 'Alisa'
]

# чтобы вывести один элемент списка, нужно обратиться к нему по индексу
print(students[3])  # Alisa
# чтобы вывести все элементы списка по одному (перебрать)
# есть два способа:
# 1. Перебор списка через индекс
for index in range(len(students)):  # количество повторений задается через длину списка
    print(f'index: {index}, element: {students[index]}')

# 2. Перебор списка через значение
for element in students:
    print(f'Element: {element}')

