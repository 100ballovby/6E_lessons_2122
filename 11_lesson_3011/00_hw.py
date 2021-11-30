# Задание 3-4
guests = ['Sarah', 'Denny', 'John']
for name in guests:
    print(f'Hello, {name}! Come to my party.')

# 3.5
print(f'{guests[0]} can not come!')
guests[0] = 'Andrew'
for name in guests:
    print(f'Hello, {name}! Come to my party.')
# 3.6
print('I can invite three more peoples.')

guests.insert(0, 'Julia')
guests.insert(1, 'Pablo')
guests.append('Vladimir')
for name in guests:
    print(f'Hello, {name}! Come to my party.')

# 3.7
print('I can invite only 2 peoples.')
while len(guests) > 2:
    guests.pop(0)
for name in guests:
    print(f'Hello, {name}! Come to my party.')

# 3.9
print(f'There is {len(guests)} peoples invited.')