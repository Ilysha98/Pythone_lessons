sum = int(input())
p = int(input())
answer = " i didn't answer."

d = sum ** 2 - 4 * p
if d >= 0:
    x_1 = (sum + d ** 0.5) // 2
    x_2 = (sum - d ** 0.5) // 2
    if x_1 * x_2 == p:
        answer = f"{x_1}, {x_2}"

print(answer)