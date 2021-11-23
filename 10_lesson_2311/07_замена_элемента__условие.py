"""Дан список чисел. Необходимо заменить все 0 на None"""
arr = [5, 6, 2, 0, 1, 6, 0, 1, 0, 8, 0]
# заменить все нули на None 
for index in range(len(arr)):
    if arr[index] == 0:
        arr[index] = None

print(arr)


