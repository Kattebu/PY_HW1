# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum = 0
temp = 0
if number < 1000 and number > 99:
    while number > 0:
        temp = number%10
        sum += temp
        number = number//10
    print(f'Сумма цифр: {sum}')
else:
    print(f'Число {number} не трехзначное')