# Задача 1. Вычислить число Пи c заданной точностью d

# import os
# import math

# os.system('cls')
# d = 0.0
# list_accur = ['0.1', '0.01', '0.001', '0.0001', '0.00001', '0.000001', '0.0000001', '0.00000001', '0.000000001', '0.0000000001', '0.0000000001']

# while True:
#     d = input('С какой точностью от 0.1 до 0.0000000001 должно быть показано число Пи?: ')
#     if d not in list_accur:
#         print('Неверно указана точность!\n')
#     else: break

# print(f'\nЧисло Пи с Вашей точностью равно = {round(math.pi, len(d.split(".")[1]))}\n')

# ****************************************************************************************************************************************************

# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import os
# import math

# os.system('cls')
# n = 0
# k = 0
# list = []

# while True:
#     try:
#         n = int(input('\nЗадайте натуральное число: '))
#         break
#     except:
#         print('Неверно указано натуральное число!!!\n')

# for i in range(1, n):
#     if n % i == 0:
#         list.append(i)

# print(f'\nСписок ВСЕХ множителей числа {n}: {list}\n')

# while k < len(list):
#     for m in range(2, list[k] - 1):
#         if list[k] % m == 0:
#             list.remove(list[k])
#             k -= 1
#             break
#     k += 1

# print(f'Список простых множителей: {list}\n')

# *********************************************************************************************************************

# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import os

# os.system('cls')
# list_a = list(map(str, input('Введите через пробел любые числа или слова: ').split()))
# i = 0

# print(f'\nВведённый Вами список: {list_a}') 

# while i < len(list_a) - 1:
#     k = i + 1
#     while k < len(list_a):
#         if list_a[i] == list_a[k]:
#             elem = list_a[i]
#             list_a = [j for j in list_a if j != elem]
#         else:
#             k += 1
#     i += 1

# print(f'\nСписок из НЕПОВТОРЯЮЩИХСЯ элементов: {list_a}\n')  

# *********************************************************************************************************************

# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# import os
# import random

# os.system('cls')

# while True:
#     try:
#         k = int(input('\nВведите натуральную степень k от 2 до 9: '))
#         if 1 < k < 10:
#             break
#         else: print('Введённая степень не находится в диапазоне 1..9 !!!')
#     except:
#         print('Неверно указана натуральная степень!\n')

# def transcript(n):
#     return "".join(["¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

# str_result = str(random.randint(0, 100)) + 'X' + transcript(k - 1) + ' + ' + str(random.randint(0, 100)) + 'X' + transcript(k - 2) + ' + ' + str(random.randint(0, 100)) + ' = 0'

# with open('file.txt', 'w', encoding = 'utf-8') as file:
#     file.write(str_result)

# print(f'\nВыражение {str_result} записано в файл file.txt!!!\n')

# *********************************************************************************************************************

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# import os
# import random

# os.system('cls')

# def form_list(file_name):
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         string = file.read().replace('+ ', '+').replace('- ', '-')
#     with open(file_name, 'r', encoding = 'utf-8') as file:
#         print(f'\nМногочлен файла {file_name}: {file.read()}')
#     return list(map(str, string.split()))

# list_first = form_list('first.txt')
# list_second = form_list('second.txt')
# result_str = ''

# def form_dic(listt, char):
#     i = 0
#     dic = dict()
#     while i < len(listt):
#         if char in listt[i]:
#             dic[listt[i][-1]] = listt[i]
#         i += 1
#     return dic

# dic1 = form_dic(list_first, 'X')
# dic2 = form_dic(list_second, 'X')

# def determ_sum(v, m):
#     digit_one = int(v.split('X')[0])
#     digit_two = int(m.split('X')[0])
#     summ = digit_one + digit_two
#     if summ == 0: return ''
#     elif summ > 0: return '+' + str(summ)
#     else: return f' {str(summ)}'

# for k, v in dic1.items():
#     for j, m in dic2.items():
#         if k == j:
#             result_str = result_str + determ_sum(v, m) + 'X' + k

# def find_simple(list_a, list_b):
#     summ = 0
#     for elem in list_a:
#         if 'X' not in elem:
#             summ += int(elem)
#     for elem in list_b:
#         if 'X' not in elem:
#             summ += int(elem)
#     if summ == 0: return ''
#     elif summ > 0: return '+' + str(summ)
#     else: return str(summ)

# final_result = result_str + find_simple(list_first, list_second)

# with open('result.txt', 'w+', encoding = 'utf-8') as file:
#         file.write(final_result + '\n')

# print(f'\nКонечная формула суммы многочленов: {final_result} записана в файл \'result.txt\'\n')