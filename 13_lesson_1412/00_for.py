""" range - генератор последовательностей чисел (для цикла for)
range(x) -> 0...x - 1 (x не входит в последовательность)
range(a, x) -> a...x - 1 (x не входит в последовательность
range(a, x, step) -> a...x - 1 (с шагом <step>)
"""
for number in range(6):  # 0, 1, 2, 3, 4, 5
    print(number, end=', ')

print()

for digit in range(10, 51):  # 10, 11, 12, 13....49, 50
    print(digit, end=', ')

print()

for step in range(1, 15, 2):  # 1, 3, 5..., 13, 15
    print(step, end=', ')
