# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal

p = input('введите число: ')
a = Decimal(p)
a = a.quantize(Decimal("1.0000"))
print(a)