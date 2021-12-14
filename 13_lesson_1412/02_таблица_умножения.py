n = int(input('Для какого числа нужна таблица? '))
stop = int(input('До какого числа нужна таблица? '))

for i in range(1, stop + 1):
    print(f'{n} * {i} = {n * i}')
