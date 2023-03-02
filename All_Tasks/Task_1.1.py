numbers = int(input("Введите число: "))
counter = 0
while numbers != 0:

    counter += numbers % 10
    numbers //= 10
print(counter, " - Сумма цифр")