import numpy as np

def dcode(binary_str, a, d):
    val_int = int(binary_str, 2)
    return a + val_int * d
def ecode(x, a, d, l):
    val_int = int(round((x - a) / d))
    return f"{val_int:0{l}b}"
a,b = map(int,input().split())
p = int(input())

l = int(np.ceil(np.log2((b - a) * (10 ** p))))
d = (b - a) / (2**l - 1) 

m = int(input())

for _ in range(2*m):
    q = input()
    if q == "TO":
        x = float(input())
        bin = ecode(x,a,d,l)
        print(bin)
    if q == "FROM":
        bs = input()
        val = dcode(bs,a,d)
        print(f"{val:.4f}")