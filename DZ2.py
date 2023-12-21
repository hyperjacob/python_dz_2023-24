
"""
Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
hex_ = ["a", "b", "c", "d", "e", "f"]
num = int(input("Введите число: "))
if num > 9:
    ost = (num,1)
    result = []
    while ost[0] != 0:
        ost = divmod(ost[0], 16)
        result.append(ost[1])
    hex_num = ""
    for el in result:
        if el < 10:
            hex_num = str(el) + hex_num
        else:
            hex_num = hex_[el-10] + hex_num
else:
    hex_num = str(num)
print("Ваше число в шестнадцатиричной системе: 0x" + hex_num, "\nПроверка: ",hex(num))

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль 
fractions
"""
from math import gcd
from fractions import Fraction
def simplification(a, b):
    a = int(a)
    b = int(b)
    quotient = gcd(a, b)
    if quotient != 1:
        a_simple = int(a/quotient)
        b_simple = int(b/quotient)
        return (a_simple, b_simple)
    else:
        return(a, b)

a, b = input('Введите первую дробь в формате "a/b": ').split("/")
c, d = input('Введите вторую дробь в формате "c/d": ').split("/")

a_numerator = simplification(a, b)[0]
a_denominator = simplification(a, b)[1]
b_numerator = simplification(c, d)[0]
b_denominator = simplification(c, d)[1]

#умножение
multiplication = simplification(a_numerator * b_numerator, a_denominator * b_denominator)
multiplication_numerator = multiplication[0]
multiplication_denominator = multiplication[1]

#cумма
sum = simplification(a_numerator * b_denominator + b_numerator * a_denominator, a_denominator * b_denominator)
sum_numerator = sum[0]
sum_denominator = sum[1]

#проверка
a_fr = Fraction(int(a), int(b))
b_fr = Fraction(int(c), int(d))


print(f"{a}/{b} + {c}/{d} = {sum_numerator}/{sum_denominator}\n"
      f"{a}/{b} * {c}/{d} = {multiplication_numerator}/{multiplication_denominator}\n"
      f"Проверка (Fraction): {a}/{b} + {c}/{d} = {a_fr + b_fr}, {a}/{b} * {c}/{d} = {a_fr * b_fr}")
