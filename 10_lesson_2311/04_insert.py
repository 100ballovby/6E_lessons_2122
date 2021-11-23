# можно вставлять элемент в список на определенное место
array = [4, 3, 5, 2, 7, 9, 1, 567]
print(f'Изначально: {array}')
array.insert(3, 'меня вставили')
# insert(index, element) вставляет element на место index, остальные сдвигаются
print(f'Теперь: {array}')
