def orientare(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


n = int(input())
    
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

p.sort()

li = [p[0], p[1]]
for i in range(3,n+1):
    while len(li) >= 2 and orientare(li[-2], li[-1], p[i-1]) <= 0:
        li.pop()
    li.append(p[i-1])

ls = [p[n-1], p[n-2]]
for i in range(n-3,-1,-1):
    while len(ls) >= 2 and orientare(ls[-2], ls[-1], p[i]) <= 0:
        ls.pop()
    ls.append(p[i])

rez = li[:-1] + ls[:-1]
print(len(rez))
for punct in rez:
    print(punct[0], punct[1])
