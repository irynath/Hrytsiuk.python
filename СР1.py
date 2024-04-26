# Завдання 1
def print_twinkle():
    twinkle_lines = [
        "Twinkle, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "How I wonder what you are"
    ]

    for line in twinkle_lines:
        print(line)
      
# Завдання 3
color_list = ["Red", "Green", "White", "Black"]

print("Перший колір:", color_list[0])

print("Останній колір:", color_list[-1])

# Завдання 4
def calculate_expression(n):
    # n + nn + nnn
    result = n + int(str(n) * 2) + int(str(n) * 3)
    return result

n = int(input("Введіть число n: "))
result = calculate_expression(n)
print("Результат обчислення:", result)

# Завдання 5
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

for num in numbers:
    if num == 237:
        break
    elif num % 2 == 0:
        print(num)
      
# Завдання 6
def check_sequence(string):
    zero_count = 0
    one_count = 0
    for char in string:
        if char == '0':
            zero_count += 1
            one_count = 0  # Скидаємо лічильник одиниць, якщо зустріли нуль
        elif char == '1':
            one_count += 1
            zero_count = 0  # Скидаємо лічильник нулів, якщо зустріли одиницю
        if zero_count == one_count and zero_count > 0:  # Перевіряємо, чи знайдено однакову послідовність
            return True
    return False

sequence1 = "01010101"
sequence2 = "00011100011"

# Перевірка
print(check_sequence(sequence1))
print(check_sequence(sequence2)) 

# Завдання 7
def print_even_numbers(n, m):
    for i in range(-n, n + 1, m):
        if i % 2 == 0:
            print(i)

m = 1
n = m * 10

# Виведення усіх парних чисел від -n до n з кроком m
print_even_numbers(n, m)

# Завдання 8
def count_password_combinations(m):
    combinations = 1
    for i in range(25, 25 - m, -1):
        combinations *= i
    return combinations

m = 1

combinations = count_password_combinations(m)
print("Кількість можливих комбінацій:", combinations)

# Завдання 9
my_list = [1, 2, 4, 5]
L = [3, 6, 7]

# а.) Розширення списку, додавши до нього усі елементи списку [3, 6, 7]
my_list.extend(L)
print("a.) Розширений список:", my_list)

# б.) Вставка на другий елемент значення 33333
my_list.insert(1, 33333)
print("б.) Список з вставкою:", my_list)

# в.) Розташування списку у зворотньому порядку
my_list.reverse()
print("в.) Список у зворотньому порядку:", my_list)

# г.) Додавання числа 3 в кінець списку
my_list.append(3)
print("г.) Список з доданою 3:", my_list)

# д.) Видалення першого елементу списку, який має значення 3
my_list.remove(3)
print("д.) Список після видалення першого елемента зі значенням 3:", my_list)

# е.) Розташування списку у порядку збільшення
my_list.sort()
print("е.) Список у порядку збільшення:", my_list)

# ж.) Очищення списку
my_list.clear()
print("ж.) Порожній список:", my_list)
