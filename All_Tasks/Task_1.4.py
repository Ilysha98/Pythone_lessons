n = int(input("Долечки"))
m = int(input("Долечки"))
k = int(input("Разлом долечек"))
if k % 2 == 1:
    print(" Не получится так сломать шоколадку ")
if n * m < k:
    print(" Nice job ")
else:
    print(" Bad job ")