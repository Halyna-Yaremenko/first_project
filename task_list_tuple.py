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

value = "1 2 65 4 34 6 96 34 2 94 3"
value_list = list(map(int, value.split()))

print(value_list[2::2])