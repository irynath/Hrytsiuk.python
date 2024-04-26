import math

# Задача 1
def square_and_fourth_power():
  """Підносить невід'ємні числа до квадрата, а від'ємні до четвертого степеня."""
  num1 = float(input("Введіть перше число: "))
  num2 = float(input("Введіть друге число: "))
  num3 = float(input("Введіть третє число: "))

  result1 = num1**2 if num1 >= 0 else num1**4
  result2 = num2**2 if num2 >= 0 else num2**4
  result3 = num3**2 if num3 >= 0 else num3**4

  print("Результати:", result1, result2, result3)

# Задача 2
def closer_to_origin():
  """Визначає, яка з двох точок ближче до початку координат."""
  x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
  x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

  distance_a = math.sqrt(x1**2 + y1**2)
  distance_b = math.sqrt(x2**2 + y2**2)

  if distance_a < distance_b:
    print("Точка A ближче до початку координат.")
  elif distance_b < distance_a:
    print("Точка B ближче до початку координат.")
  else:
    print("Точки A і B знаходяться на однаковій відстані від початку координат.")

# Задача 3
def triangle_check():
  """Перевіряє, чи існує трикутник з заданими кутами і чи є він прямокутним."""
  angle1 = float(input("Введіть перший кут трикутника (в градусах): "))
  angle2 = float(input("Введіть другий кут трикутника (в градусах): "))

  if angle1 + angle2 >= 180:
    print("Трикутник з такими кутами не існує.")
  else:
    angle3 = 180 - angle1 - angle2
    print("Третій кут трикутника:", angle3)
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
      print("Трикутник прямокутний.")
    else:
      print("Трикутник не прямокутний.")

# Задача 4
def replace_numbers():
  """Замінює числа згідно з умовами."""
  x = float(input("Введіть число x: "))
  y = float(input("Введіть число y: "))

  if x != y:
    if x < y:
      x = (x + y) / 2
      y = 2 * x * y
    else:
      y = (x + y) / 2
      x = 2 * x * y
  else:
    x = 0
    y = 0

  print("Нові значення x і y:", x, y)

# Задача 5
def point_location():
  """Визначає розташування точки на площині."""
  x, y = map(float, input("Введіть координати точки A (x, y): ").split())

  if x == 0 and y == 0:
    print("Точка A знаходиться в початку координат.")
  elif x == 0:
    print("Точка A знаходиться на осі Y.")
  elif y == 0:
    print("Точка A знаходиться на осі X.")
  elif x > 0 and y > 0:
    print("Точка A знаходиться в першому координатному куті.")
  elif x < 0 and y > 0:
    print("Точка A знаходиться в другому координатному куті.")
  elif x < 0 and y < 0:
    print("Точка A знаходиться в третьому координатному куті.")
  else:
    print("Точка A знаходиться в четвертому координатному куті.")

# Задача 6
def replace_equal_numbers():
  """Замінює числа згідно з умовами."""
  a = int(input("Введіть ціле число a: "))
  b = int(input("Введіть ціле число b: "))

  if a != b:
    a = max(a, b)
    b = max(a, b)
  else:
    a = 0
    b = 0

  print("Нові значення a і b:", a, b)

# Задача 7
def count_negative():
  """Підраховує кількість від'ємних чисел."""
  a, b, c = map(float, input("Введіть три числа (a, b, c): ").split())
  count = sum(1 for num in (a, b, c) if num < 0)
  print("Кількість від'ємних чисел:", count)

# Задача 8
def count_positive():
  """Підраховує кількість додатних чисел."""
  a, b, c = map(float, input("Введіть три числа (a, b, c): ").split())
  count = sum(1 for num in (a, b, c) if num > 0)
  print("Кількість додатних чисел:", count)

# Задача 9
def count_integers():
  """Підраховує кількість цілих чисел."""
  a, b, c = map(float, input("Введіть три числа (a, b, c): ").split())
  count = sum(1 for num in (a, b, c) if num == int(num))
  print("Кількість цілих чисел:", count)

# Задача 10
def find_divisors():
  """Визначає, дільником яких чисел є задане число k."""
  a, b, c = map(int, input("Введіть три цілих числа (a, b, c): ").split())
  k = int(input("Введіть ціле число k: "))

  divisors = []
  for num in (a, b, c):
    if num % k == 0:
      divisors.append(num)

  if divisors:
    print("Число k є дільником чисел:", *divisors)
  else:
    print("Число k не є дільником жодного з чисел a, b, c.")

# Виклик функцій для виконання завдань
square_and_fourth_power()
closer_to_origin()
triangle_check()
replace_numbers()
point_location()
replace_equal_numbers()
count_negative()
count_positive()
count_integers()
find_divisors()
