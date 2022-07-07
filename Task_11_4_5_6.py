import sys
def is_digit(string):
  if string.isdigit():
    return True
  else:
    try:
      float(string)
      return True
    except ValueError:
      return False
class NumbersOnly(Exception):
  def __init__(self,txt):
    self.txt = txt
class Warehouse:
    def __init__(self,price, firm):
        self.price = price
        self.firm = firm


class Office_equipment:
    def __init__(self, price, firm):
        self.price = price
        self.firm = firm

class Printer(Office_equipment):
    def __init__(self, price, firm, model):
        super().__init__(price, firm)
        self.model = model
    def shipping_to_the_warehouse(self):
        try:
            if is_digit(self.price) == False:
                raise NumbersOnly('Это не число!')
            print(f'Принтер, модель {self.model}, производитель {self.firm} по цене {self.price} отправлен на склад')
        except NumbersOnly as err:
            print(err)
    def __str__(self):
        return (f'Принтер, модель {self.model}, производитель {self.firm} по цене {self.price}')


class Scanner(Office_equipment):
    def __init__(self, price, firm, model):
        super().__init__(price, firm)
        self.model = model
    def shipping_to_the_warehouse(self):
        try:
            if is_digit(self.price) == False:
                raise NumbersOnly('Это не число!')
        except NumbersOnly as err:
            print(err)
        else:
            print(f'Сканер, модель {self.model}, производитель {self.firm} по цене {self.price} отправлен на склад')
    def __str__(self):
        return (f'Сканер, модель {self.model}, производитель {self.firm} по цене {self.price}')

class Xerox(Office_equipment):
    def __init__(self, price, firm, model):
        super().__init__(price, firm)
        self.model = model
    def shipping_to_the_warehouse(self):
        try:
            if is_digit(self.price) == False:
                raise NumbersOnly('Это не число!')
        except NumbersOnly as err:
            print(err)
        else:
            print(f'Ксерокс, модель {self.model}, производитель {self.firm} по цене {self.price} отправлен на склад')
    def __str__(self):
        return (f'Ксерокс, модель {self.model}, производитель {self.firm} по цене {self.price}')

p = Printer('3.50','Panasonic','X-30')
p.shipping_to_the_warehouse()
s = Scanner('4.80','Datalogic', 'p800')
s.shipping_to_the_warehouse()
x = Xerox('1.45', 'Canon', 'rr460')
x.shipping_to_the_warehouse()
print(p)
print(s)
print(x)