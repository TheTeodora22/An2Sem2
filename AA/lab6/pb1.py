class pt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, p):
        return pt(self.x - p.x, self.y - p.y)
    def cross(self, p):
        return self.x * p.y - self.y * p.x
    def dot(self, p):
        return self.x * p.x + self.y * p.y
    def sqrLen(self):
        return self.x * self.x + self.y * self.y

seq = []
translation = None
n = 0

def prepare(points):
    global n, seq, translation
    n = len(points)
    pos = 0
    for i in range(1, n):
        if points[i].x < points[pos].x or (points[i].x == points[pos].x and points[i].y < points[pos].y):
            pos = i
    points = points[pos:] + points[:pos]
    if n > 2 and (points[1] - points[0]).cross(points[n - 1] - points[0]) < 0:
        points = [points[0]] + points[1:][::-1]

    translation = points[0]
    n -= 1
    seq = [points[i + 1] - translation for i in range(n)]

def on_segment(a, b, p):
    ab = b - a
    ap = p - a
    if ab.cross(ap) != 0:
        return False
    t = ap.dot(ab)
    return 0 <= t <= ab.sqrLen()

def pointInConvexPolygon(point):
    point = point - translation
    cp_first = seq[0].cross(point)
    cp_last = seq[n - 1].cross(point)
    if cp_first == 0:
        if point.dot(seq[0]) < 0:
            return "OUTSIDE"
        if point.sqrLen() <= seq[0].sqrLen():
            return "BOUNDARY"
    if cp_last == 0:
        if point.dot(seq[n - 1]) < 0:
            return "OUTSIDE"
        if point.sqrLen() <= seq[n - 1].sqrLen():
            return "BOUNDARY"
    if cp_first == 0 and cp_last == 0:
        t = point.dot(seq[n - 1])
        if t < 0:
            return "OUTSIDE"
        return "BOUNDARY" if t <= seq[n - 1].sqrLen() else "OUTSIDE"
    if cp_first < 0 or cp_last > 0:
        return "OUTSIDE"
    l, r = 0, n - 1
    while r - l > 1:
        mid = (l + r) // 2
        if seq[mid].cross(point) >= 0:
            l = mid
        else:
            r = mid
    
    edge = (seq[l + 1] - seq[l]).cross(point - seq[l])
    if seq[l].cross(point) == 0 and l > 0 and on_segment(seq[l - 1], seq[l], point):
        return "BOUNDARY"
    if edge < 0:
        return "OUTSIDE"
    elif edge == 0:
        return "BOUNDARY" if on_segment(seq[l], seq[l + 1], point) else "OUTSIDE"
    else:
        return "INSIDE"

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(pt(x, y))

prepare(points)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    point = pt(x, y)
    print(pointInConvexPolygon(point))