# Наданий код порівнює кількість операцій, потрібних для лінійного та бінарного пошуку у випадкових списках довжиною '''n'''.
# Визначте, (в середньому) у скільки разів менше потрібно операцій для виконання бінарного пошуку для різних довжин списків.
# Для цього:
# 1. Запустіть програму 5 разів зі значенням довжини '''n=3'''. Запишіть результати та порахуйте:
# * скільки операцій (в середньому) потрібно для лінійного пошуку
# * скільки операцій (в середньому) потрібно для бінарного пошуку
# * у скільки разів менше потрібно операцій для бінарного пошуку, порівняно з лінійним пошуком
# 2. Повторіть розрахунки для:
# * '''n=10'''
# * '''n=100'''
# * '''n=1000'''
# 3. Залиште коментар з результатами порівняння в Google Classroom.


from random import *

print("Введіть довжину випадкового списку:")
n = int(input())

numbers = choices(range(n), k=n)
target = choice(range(n))

# Лінійний (послідовний) пошук
linear_search_operations = 0
i = 0
found = None
while found == None and i < len(numbers):
    linear_search_operations = linear_search_operations + 1
    
    if numbers[i] == target:
        found = i
    i = i + 1

print("Кількість операцій під час лінійного пошуку:", linear_search_operations)

# Бінарний пошук
binary_search_operations = 0
numbers.sort()
left = 0
right = len(numbers) - 1
found = None

while found == None and left <= right:
    binary_search_operations = binary_search_operations + 1

    mid = int((left + right) / 2)

    if numbers[mid] == target:
        found = mid
    else:
        if numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
print("Кількість операцій під час бінарного пошуку:", binary_search_operations)



