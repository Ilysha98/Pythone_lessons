sideFirst = 0
sideSecond = 0
n = int(input("Укажите количество монет на столе "))

for i in range(n):
    counter = int(input())
    if counter:
        sideFirst += 1
    else:
        sideSecond += 1

if sideFirst > sideSecond:
    print(sideSecond)
else:
    print(sideFirst)
