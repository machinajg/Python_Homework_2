# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# # Способ 1
# n = int (input('Введите количество монеток n: '))
# heads = 0
# tails = 0
# for i in range(n): 
#     x = int(input()) 
#     if x == 1:
#         heads += 1
#     else:
#         tails += 1        
# if heads > tails:
#     print (f"Tails: {tails}")
# else:
#     print (f"Heads: {heads}")    
    

# Способ 2 
n = int (input('Введите количество монеток n: '))
from random import randint
coins = [randint(0,1) for i in range(n)]    #  Создаём список и заполняем 0 и 1 рандомно
print(coins)
heads = 0
tails = 0
for i in (coins):                   #  либо:    for i in range(n):
    if i == 0:                      #               if coins[i] == 0:
        heads += 1                  #                   heads += 1
    else:                           #                   и т.д.
        tails += 1
if heads > tails:
    print (f"Tails: {tails}")
else:
    print (f"Heads: {heads}")
