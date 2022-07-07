import sys
class NumbersOnly(Exception):
  def __init__(self,txt):
    self.txt = txt
def is_digit(string):
  if string.isdigit():
    return True
  else:
    try:
      float(string)
      return True
    except ValueError:
      return False
i = 0
new_list = []
while i < 10:
  i +=1
  num = input('Введите число: ')
  if num == 'stop':
    sys.exit()
  try:
    if is_digit(num) == False:
      raise NumbersOnly('Это не число!')
    new_list.append(num)
  except NumbersOnly as err:
    print(err)
  else:
    print(new_list)