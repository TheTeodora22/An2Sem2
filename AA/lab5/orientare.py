line = input()
    
t = int(line)
for _ in range(t):
    date = input().split()
            
    xp, yp = int(date[0]), int(date[1])
    xq, yq = int(date[2]), int(date[3])
    xr, yr = int(date[4]), int(date[5])

    val = (xq - xp) * (yr - yp) - (yq - yp) * (xr - xp)

    if val > 0:
        print("LEFT")
    elif val < 0:
        print("RIGHT")
    else:
        print("TOUCH")
