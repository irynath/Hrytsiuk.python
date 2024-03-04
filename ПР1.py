input_str = input("Ввести 3 невід'ємних цілих числа a, z, x розділені пробілами: ")

values = input_str.split()

if len(values) != 3:
    print("Потрібно ввести рівно 3 числа!")
    exit()

try:
    a = int(values[0])
    z = int(values[1])
    x = int(values[2])
except ValueError:
    print("Введені значення повинні бути цілими числами!")
    exit()

if a < 0 or z < 0 or x < 0:
    print("Числа повинні бути невід'ємними!")
    exit()

Y = (1 - z) * (x ** 0.5) / (a - (1 / (1 + x) ** 0.5))

print("Результат обчислення формули: ", Y)
