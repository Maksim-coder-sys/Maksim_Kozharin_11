class ZeroDivision_Error(Exception):
  def __init__(self,txt):
    self.txt = txt

divisible = input('Введите делимое: ')
divider = input('Введите делитель: ')
try:
  divisible = int(divisible)
  divider = int(divider)
  if divider == 0:
    raise ZeroDivision_Error('На ноль делить нельзя')
  res = divisible/divider
except ValueError:
  print('Вы ввели не число')
except ZeroDivision_Error as err:
  print(err)
else:
  print(f'Все хорошо. Деление выполнено. Результат: {res}')