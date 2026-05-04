
line = input()

n = int(line)
puncte = []

for _ in range(n):
    puncte.append(list(map(int, input().split())))

puncte.append(puncte[0])

stanga = 0
dreapta = 0
coliniare = 0

for i in range(n - 1):
    p1 = puncte[i]
    p2 = puncte[i + 1]
    p3 = puncte[i + 2]

    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    if val > 0:
        stanga += 1
    elif val < 0:
        dreapta += 1
    else:
        coliniare += 1

print(stanga, dreapta, coliniare)
