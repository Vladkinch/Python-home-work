# 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randint

list = [randint(0,15) for i in range (10)]
print(list)
new_list =[]
[new_list.append(i) for i in list if i not in new_list ]
print(new_list)

