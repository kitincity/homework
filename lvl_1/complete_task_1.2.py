from random import randint
import datetime

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

print('\nПункт A:')

sum = 0

l = len(my_favorite_songs)

for number in range(3):
    r = randint(0, l-1)

    sum+=my_favorite_songs[r][1]


print('Три песни звучат', sum, 'минут')

#sum+=

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

print('\nПункт B:')

sum = 0

keys = list(my_favorite_songs_dict)

for number in range(3):
    r = randint(0, len(keys)-1)

    sum+=my_favorite_songs_dict.get(keys[r])


print('Три песни звучат', sum, 'минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random


print('\nПункт C:')
for number in range(3):
    r = randint(0, l-1)
    print(my_favorite_songs[r][0], my_favorite_songs[r][1])

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

print('\nПункт D:')
for number in range(l):
    time = str(my_favorite_songs[number][1])
    time = time.split('.')
    print(my_favorite_songs[number][0], datetime.time(0,int(time[0]),int(time[1])))