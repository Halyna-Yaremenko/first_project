

#Ви придбали товар на певну суму s. Скільки купюр різного номіналу треба віддати продавцю, якщо починати платити з найбільших? У вас є 1, 2, 5, 10, 100, 500 гривень.

# sum = int(input('Enter sum: '))

# sum_500 = sum // 500
# sum = sum % 500

# sum_100 = sum // 100
# sum = sum % 100

# sum_10 = sum // 10
# sum = sum % 10

# sum_5 = sum // 5
# sum = sum % 5

# sum_2 = sum // 2
# sum = sum % 2

# sum_1 = sum // 1
# sum = sum % 1

# print ('500: ', sum_500)
# print ('100: ', sum_100)
# print ('10: ', sum_10)
# print ('5: ', sum_5)
# print ('2: ', sum_2)
# print ('1: ', sum_1)

# Розгалудження

# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..

# password = input ('Enter Password: ')
# password_accept = 'QwerTy'

# if password == password_accept:
#     print ('Password accepted!')
# else:
#     print ('Sorry, that is the wrong password.')

# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.

# name1 = input ('Enter name1: ')
# name2 = input ('Enter name2: ')

# if name1 <= name2:
#     print (name1, name2)
# else:
#     print (name2, name1)


# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

# number = int(input('Enter number: '))

# if number == 1:
#     name_of_namber = 'One'
# elif number == 2:
#     name_of_namber = 'Two'
# elif number == 3:
#     name_of_namber = 'Three'
# else:
#     name_of_namber = 'Unknown'

# print(name_of_namber)

# Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.

# letter1 = input ('Enter letter1: ').lower()
# letter2 = input ('Enter letter2: ').lower()

# if letter1 <= letter2:
#     print ('First letter:', letter1, 'Second letter:', letter2)
# else:
#     print ('First letter:', letter2, 'Second letter:', letter1)

# якщо реєстр важливий

# letter1 = input ('Enter letter1: ')
# letter2 = input ('Enter letter2: ')

# if letter1.lower() == letter2.lower():
#     if letter1 < letter2:
#         print ('First letter:', letter1, 'Second letter:', letter2)
#     else:
#          print ('First letter:', letter2, 'Second letter:', letter1)
# elif letter1.lower() < letter2.lower():
#     print ('First letter:', letter1, 'Second letter:', letter2)
# else:
#     print ('First letter:', letter2, 'Second letter:', letter1)


# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

# temperature = float(input('Enter temperature in °C: '))

# if temperature <= 0:
#    print ('A cold, isn’t it?')
# elif temperature > 0 and temperature < 10:
#    print ('Cool')
# else:
#     print ('Nice weather we are having')


# Середній рівень

# Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.

# number = int(input('Enter the number of sides of the shape: '))

# if number == 3:
#     print('This is a triangle.')
# elif number == 4:
#     print('This is a square.')
# elif number == 5:
#     print('This is a pentagon.')
# elif number == 6:
#     print('This is a hexagon.')
# else:
#     print ('Number of pages entered outside the limits')

# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

# number = int(input('Enter number from 0 to 36: '))

# if number >= 0 and number <= 36:

#    if number == 0:
#       print ('Green')

#    if number >= 1 and number <= 10:
      
#       if number % 2 == 0:
#          print ('Black')
#       else:
#          print ('Red')

#    if number >= 11 and number <= 18:
      
#       if number % 2 == 0:
#          print ('Red')
#       else:
#          print ('Black')

#    if number >= 19 and number <= 28:
      
#       if number % 2 == 0:
#          print ('Black')
#       else:
#          print ('Red') 

#    if number >= 29 and number <= 36:
      
#       if number % 2 == 0:
#          print ('Red')
#       else:
#          print ('Black')

# else:
#    print ('The number is not in the range from 0 to 36')


# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

# x1 = int(input('Enter the coordinates of point A, x: '))
# y1 = int(input('Enter the coordinates of point A, y: '))
# x2 = int(input('Enter the coordinates of point B, x: '))
# y2 = int(input('Enter the coordinates of point B, y: '))

# if ((x1 ** 2 + y1 ** 2)) ** 1/2 == ((x2 ** 2 + y2 ** 2)) ** 1/2:
#    print ('The distance is the same ') 

# elif ((x1 ** 2 + y1 ** 2)) ** 1/2 > ((x2 ** 2 + y2 ** 2)) ** 1/2:
#       print ('A')
# else:
#       print ('B')
   

# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.

# x = int(input('Enter the coordinates of point A, x: '))
# y = int(input('Enter the coordinates of point A, y: '))
# r = int(input('Enter the radius of the circle,   r: '))

# if (x ** 2 + y ** 2) <= r ** 2:
#     print('The point is inside the circle')
# else:
#     print('The point is outside the circle')


# Дано натуральное число. Визначити, чи закінчується число парною цифрою.

# number = int(input('Enter number: '))

# last_number = number % 10

# if last_number % 2 == 0:
#     print('True')
# else:
#     print('False')


# Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.


# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
# -3
# 2
# 4
# 2
# Вихідні дані:
# No roots.
# 0.27 and -3.05
# -1.00

# Напишіть програму, щоб визначити, чи задане ціле число (вводиться користувачем) парне або непарне.

# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print('True')
# else:
#     print('False')


# Відомі рік і номер місяця народження людини, а також рік і номер місяця сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.

# year_birth = int(input('Enter year of birth: '))
# month_birth = int(input('Enter month of birth (1-12): '))

# year_now = int(input('Enter year today : '))
# month_now = int(input('Enter month today (1-12): '))

# age = year_now - year_birth

# if month_now < month_birth:
#     age -= 1
# print (f'Full age: {age}')


# Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.

# number = input('Enter a four-digit number: ')

# result = ""

# for digit in number:
    
#     if int(digit) % 2 == 0:  
#         result += "*"
#     else:                    
#         result += digit

# print(f'Result: {result}')

