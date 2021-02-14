# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):

    def __init__(self, txt=""):
        self.txt = txt


try:
    user_answer = input("Введите делимое и делитель через запятую:\n>>>").split(",")
    dividend, divider = user_answer
    dividend = float(dividend)
    divider = float(divider)
    if divider == 0:
        raise MyZeroDivisionError()
except ValueError as error:
    print(f"Введены некорректные данные: {error}")
except MyZeroDivisionError as error:
    print("На ноль делить нельзя!")
    print("Результат деления: ", float("nan"))
else:
    quotient = dividend / divider
    print(f"Данные введены верно: {dividend}/{divider} = {quotient}")