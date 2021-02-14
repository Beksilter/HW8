# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, user_date):
        self.user_date = user_date
        Date.date_to_int(self.user_date)

    @classmethod
    def date_to_int(cls, user_date):
        try:
            number = int(user_date[0:user_date.index("-")])
            user_date = user_date[user_date.index("-") + 1:]
            month = int(user_date[0:user_date.index("-")])
            year = int(user_date[user_date.index("-") + 1:])
            Date.validation(number, month, year)
        except ValueError:
            print("Ошибка! Дата должна передаваться в формате \"ЧЧ-ММ-ГГГГ\".")

    @staticmethod
    def validation(number, month, year):
        if not 1 <= number <= 31:
            print("Ошибка в записи числа.")
        elif not 1 <= month <= 12:
            print("Ошибка в записи месяца.")
        elif year < 2021:
            print(f"Получена дата {number:02}.{month:02}.{year} г. Дата из прошлого")
        elif year > 2021:
            print(f"Получена дата {number:02}.{month:02}.{year} г. Дата из будущего")
        else:
            print(f"Получена дата {number:02}.{month:02}.{year} г.")


d1 = Date("30-07-1991")
d2 = Date("1-01-2000")
d3 = Date("41-12-2019")
d4 = Date("11-18-2019")
d5 = Date("1-12-200019")
d6 = Date("01-11-2019")
d7 = Date("01-11-2o19")
d8 = Date("111-1-2019")