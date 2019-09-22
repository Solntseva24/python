# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [5, 8, 7, 14, 3, 4, 9]
numbers_2 = [i ** 2 for i in numbers]
print(numbers_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits = ['яблоко', 'апельсин', 'персик', 'груша']
fruits_2 = ['киви', 'апельсин', 'персик', 'банан']

list = [i for i in fruits if i in fruits_2]
print(list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list = [5, 3, 6, 8, 12, 15, -8, -4, 1, 16, 24]

list_2 = [i for i in list if not i % 3 if i >= 0 if i % 4]
print(list_2)
