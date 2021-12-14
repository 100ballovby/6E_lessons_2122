for n in range(11):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f'{n}! = {factorial}')