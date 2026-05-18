def orientare(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def pe_segment(p1, p2, p):
    return min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])

def intersect(p1, p2, p3, p4):

    o1 = orientare(p1, p2, p3)
    o2 = orientare(p1, p2, p4)
    o3 = orientare(p3, p4, p1)
    o4 = orientare(p3, p4, p2)

    if ((o1 > 0 and o2 < 0) or (o1 < 0 and o2 > 0)) and ((o3 > 0 and o4 < 0) or (o3 < 0 and o4 > 0)):
        return True
    return False


n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

m = int(input())
for _ in range(m):
    px, py = map(int, input().split())
    p = (px, py)

    boundery = False
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]  # Următorul vârf (asigură închiderea poligonului)
        
        if orientare(p1, p2, p) == 0 and pe_segment(p1, p2, p):
            boundery = True
            break

    if boundery:
        print("BOUNDARY")
    else:
        max_x = max(pt[0] for pt in points)
        max_y = max(pt[1] for pt in points)
        
        mx = max_x + 5
        my = max_y + 5
        M = (mx, my)
        
        valid = False
        while not valid:
            valid = True
            for pt in points:
                if orientare(p, M, pt) == 0:  
                    my += 1
                    M = (mx, my)
                    valid = False
                    break  

        intersectii = 0
        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            
            if intersect(p, M, p1, p2):
                intersectii += 1

        if intersectii % 2 == 1:
            print("INSIDE")
        else:
            print("OUTSIDE")