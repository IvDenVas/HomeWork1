# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))
if num < 0: print('Число не должно быть отрицательным!')
elif num < 100 or num > 999: print('Число должно быть трехзначным!')
else: print(f'{num} -> {num // 100 + num // 10 % 10 + num %10} ({num // 100} + {num // 10 % 10} + {num % 10})')