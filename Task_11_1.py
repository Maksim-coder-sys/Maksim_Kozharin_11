import datetime


class Date:
    def __init__(self, date_time):
        self.date_time = date_time

    @classmethod
    def classmethod(cls, date_time):
        int_date = int(''.join(date_time.split('-')))
        print(int_date)
        cls.staticmethod(int_date)
    @staticmethod
    def staticmethod(int_date):
        if 0 < int_date // 10000 % 100 < 13:
            print("Число месяцев в году валидно")
        else:
            print("Число месяцев в году  не валидно")
        if 0 < int_date // 1000000 < 32:
            print("Число дней в месяце валидно")
        else:
            print("Число дней в месяце не валидно")


date_time = datetime.datetime.today().strftime('%d-%m-%Y')
Date.classmethod(date_time)

