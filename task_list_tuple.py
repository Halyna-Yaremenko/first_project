# [1, "q", 2.0]    # list
# list((1, 5, "y"))  # tuple nezminnui - kortez
# s.append(7) # dodatu element v kinez lista
# v_list = value_list[-2:]
# print(v_list)
# v_list.extend(v_l2) # dodatu list v kinez
# print(v_list)

# 1. Створіть список на основі введеної послідовності цілих чисел і надрукуйте другу половину списку. Якщо кількість не парна, то вивести більшу кількість.

# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))
# print(value_list[len(value_list) // 2:])


# 2. Створіть список на основі введеної послідовності цілих чисел і надрукуйте його елементи таким чином: два останні елементи переміщені з кінця в початок списку без зміни їх початкового порядку.

# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))

# result = value_list[-2:] + value_list[:-2]
# print(result)

# 3. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.

# langueges = "english german ukrainian russian polish french portugeese spanish danish norvegian"

# lang_list = langueges.split()

# lang_list.sort().          
# print(" ".join(lang_list))

# .sort  не змінює рядок, просто його запамятовує
# sorted() змінює і запамятовує новий відсортований список

# 4. Виведіть елементи даного списку в зворотному порядку, не змінюючи сам список.

# langueges = "english german ukrainian russian polish french portugeese spanish danish norvegian"

# lang_list = langueges.split()

# print(" ".join(sorted(lang_list, reverse=True)))

# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

# value = "1 2 65 4 34 6 96 34 2 94 3"
# value_list = list(map(int, value.split()))

# print(value_list[2::2])

# 6. Визначте, скільки різних слів у введеному рядку.

# text = "New Delhi New York Paris Prague Reykjavik"

# text = "Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend"

# text = text.split()
# new_text = []

# for el in text:
#     if el not in new_text:
#         new_text.append(el)

# print(len(new_text))

# --------------

# text = text.split()

# res = len(text)

# for el in range(len(text)):
 
#        for i in range(el + 1, len(text)):
      
#            if text[el] == text[i]:
#                res -= 1
#                break
                

# print(res)

# ----------------

# text = "New Delhi New York Paris Prague Reykjavik"

# text = text.split()

# print(len(set(text))) # Set {} - mnozuna, bez povtoriv!!!!! bez indexiv
       

# 7. Напишіть програму, яка приймає послідовність чисел, розділених комами, від користувача і створює список і кортеж з цими числами.

# numbers =  "7, 9, 12, 4"
# numbers = input("Enter numbers: ")
# numbers_list = list(map(int, numbers.split(", ")))

# print(numbers_list)
# print(tuple(numbers_list))

# Вхідні дані:
# 7, 9, 12, 4

# Вихідні дані:
# [7, 9, 12, 4]
# (7, 9, 12, 4)


# 8. Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.

# url = "https://www.namesite.com/folder/index.html"

# url_list = url.split("/")
# print(url_list[len(url_list)-1])

# Вхідні дані:
# https://www.namesite.com/folder/index.html

# Вихідні дані:
# index.html


# Middle level

# 9. Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.

# def set_numbers (numbers):
#      min_index = numbers.index(min(numbers))
#      max_index = numbers.index(max(numbers))

#      numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

#      return numbers

# numbers = "1 2 3 6 8 4 9 3 22 67 87"
# numbers = list(map(int, numbers.split()))

# print(numbers)
# print(set_numbers(numbers))

# 10. Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

# def task10():

#     lines = []

#     while True:
#        line = input("Enter text: ")
#        if line == "":
#             break

#        lines.append(line.upper())

#     for el in lines:
#         print(el)  

# task10()

# -----
# while input() != "":
#     print()
# -------
# a = " "
# while a != "":
#     a = input()
# -------

# run = True       # logichna/LAGIDNA zupinka zukly
# while run:
#     line = input("Enter text: ")
#     if line == "":
#         run = False


# 11. У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.

# numbers = [1, -2, -3, 5, 6, -3, 7, 8]

# for i in range(len(numbers)-1):
#     if (numbers[i] * numbers[i+1]) > 0:
#         print(numbers[i], numbers[i+1])

# Вхідні дані:
# 1 -2 -3 5 6 -3 7 8

# Вихідні дані:
# -2 -3
# 5 6
# 7 8

# 12. Напишіть програму для обчислення добутку цілих чисел (без використання циклу for), які вводяться через пропуск користувачем в одному рядку.

# numbers = "5 5 3"
# numbers_list = list(map(int, numbers.split()))

# res = 1

# while numbers_list:
#     res *= numbers_list.pop()   # множимо на останній елемент і видаляємо його зі списку

# print(res)   

# ------
# n = 0
# res = 1

# while n > len(numbers):
#    res *=numbers[n]
#    n += 1
# print(res)


# Вхідні дані:
# 2 5 3

# Вихідні дані:
# 30


# 13. Напишіть програму для друку елементів певного цілочисельного списку після видалення з нього парних чисел. Значення списку вводяться через пропуск в одному рядку.

# numbers = "3 44 6 8 9 12 7"
# numbers_list = list(map(int, numbers.split()))

# res_list = []

# # for i in numbers_list:
# #     if i % 2 != 0:
# #         res_list.append(i)

# res_list = [i for i in numbers_list if i % 2 != 0]
    
# print(res_list)


# Вхідні дані: 3 44 6 8 9 12 7
# Вихідні дані: [3, 9, 7]


# 14. Напишіть програму, яка приймає послідовність 4-цифрових двійкових чисел, розділених комами, і друкує числа, які ділиться на 5 без остачі, в рядку і розділені комами.

# numbers = "0100,0011,1010,1001,1100"
# numbers_list = numbers.split(",")
# # print(numbers_list)


# res_list = []

# for i in numbers_list:

#     st = 0
#     dec = 0
  
#     for digit in i[::-1]:
       
#         st += 1
#         dec += int(digit) * (2  ** st)
       
#     if dec % 5 == 0:
#         res_list.append(i)

# print(res_list)


# Вхідні дані: 0100,0011,1010,1001,1100
# Вихідні дані: 1010


# 15. Ви вирішили написати перетворювач коду на Python в код на Java. Так як на Java прийнятий стандарт найменування CamelCase, то ви вирішили навчитися перетворювати імена з underscore в цей формат. Стиль underscore характеризується тим, що слова в імені пишуться маленькими літерами і розділяються між собою символом підкреслення _. Стиль CamelCase означає, що кожне слово пишеться з великої літери і роздільників між словами немає. Отже, вводиться один рядок, що містить ім’я, записане в форматі underscore. Програма виводить рядок, що містить ім’я в форматі CamelCase.

# text_underscore = "my_class"
# text_CamelCase = text_underscore.title()

# print("".join(text_CamelCase.split("_")))

# Вхідні дані: my_class
# Вихідні дані: MyClass

# 16. Напишіть програму для видалення кожного третього елемента із цілочисельного списку і друку результуючого списку, доки список не стане порожнім. Початковий список цілих чисел вводиться в одному рядку через пропуск.

# numbers = "2 5 8 9 4 78 7 1"
# numbers_list = list(map(int, numbers.split()))

# index = 2

# while numbers_list:
#     index = 2
#     index %= len(numbers_list)
#     # index2 = index % len(numbers_list)
#     numbers_list.pop(index)
#     print(numbers_list)

# Вхідні дані:# 2 5 8 9 4 78 7 1
# Вихідні дані:

# [2, 5, 9, 4, 78, 7, 1]
# [2, 5, 4, 78, 7, 1]
# [2, 5, 78, 7, 1]
# [2, 5, 7, 1]
# [2, 5, 1]
# [2, 5]
# [5]
# []


# 17. Користувач вводить два цілих додатних числа n і m. Напишіть програму, яка створює двовимірний масив розміром n x m і заповнює його символами . і * у шаховому порядку (як у вихідних даних). Лівий верхній кут повинен мати символ ..

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

# for row in range(n):
#     for col in range(m):
#         if (row + col) % 2 == 0:
#            print(".", end=" ")
#         else:
#             print("*", end=" ")
    
#     print()


# Вхідні дані:
# 6 8 

# Вихідні дані:

# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .




# Hard level

# 18. У рядку через кому перераховані слова. Сформувати з цих слів новий рядок. Слова мають бути відсортовані за спаданням (від Z до A) без урахування регістру і записані через пропуск.

# text = "horse, cat, parrot, Goldfish, dog"
# # text_list = text.split(", ")
# text_list = text.split(",")
# text_list = [w.strip() for w in text_list] # strip прибирає пробіл на початку і в кінці рядка 

# text_list.sort(key=str.lower, reverse=True)

# print(" ".join(text_list))

# Вхідні дані:
# horse, cat, parrot, goldfish, dog

# Вихідні дані:
# parrot horse goldfish dog cat

# 19. Напишіть програму, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5... (число повторюється стільки разів, чому дорівнює). На вхід програми передається невід’ємне ціле число n - стільки елементів послідовності повинна надрукувати програма. На виході очікується послідовність чисел, записаних через пропуск в один рядок.

# Вхідні дані:

# 8
# Вихідні дані:

# 1 2 2 3 3 3 4 4


# 20. Використовуючи поняття списку, напишіть програму, яка створює 3D масив елементів a x b x c, кожен з яких має значення 0. Значення a, b, c вводяться в одному рядку через пропуск.

# Вхідні дані:

# 2 3 3
# 4 4 4
# Вихідні дані:

# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]
# [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
# В один ряд поставили n кеглів, пронумерувавши їх зліва направо числами від 1 до n. Потім в цей ряд кинули k куль, при цьому i-та куля збила всі кеглі з номерами від m до h включно. Визначте, які кеглі залишилися стояти на місці. Програма отримує на вхід кількість кеглів n і кількість кидків k. Далі йде k пар чисел m, h, при цьому 1 ≤ m ≤ h ≤ n ≤ 100. Програма повинна вивести послідовність з n символів, де j-й символ є I, якщо j-та кегля залишилася стояти, або ., якщо j-та кегля була збита.

# Вхідні дані:

# 10 3
# 8 10
# 2 5
# 3 6
# Вихідні дані:

# I.....I...

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

# result = []

# for row in range(n):
    
#     el_list = []
    
#     for col in range(m):
        
#         if (row + col) % 2 == 0:
#           el_list.append(".")
#         else:
#             el_list.append("*")

#     result.append(el_list)

    
# print(result)

# # lis[2][7] звернення до елементу масива