import time
n, m = map(int, input().split())
a, b, d = map(int, input().split()) # (y, x)
maps = []
for i in range(m):
    maps.append(list(map(int, input().split())))
mt = 0
cnt = 0
result = 0
maps[a][b] = -1
while 1:
    if cnt == 4:
        print("--------------------------------------")
        if d == 0:
            a = a+1
        elif d == 1:
            b = b-1
        elif d == 2:
            a = a-1
        else:
            b = b+1
        if maps[a][b] == 1:
            print(result, "#3")
            break
        cnt = 0
    if d == 0:
        d = 3
    else:
        d -= 1
    if d == 0:
        mt = (a-1, b)
    elif d == 1:
        mt = (a, b+1)
    elif d == 2:
        mt = (a+1, b)
    else:
        mt = (a, b-1)
    
    if maps[mt[0]][mt[1]] == 1 or maps[mt[0]][mt[1]] == -1:
        print("cnt",mt[0],mt[1])
        print("abd",a,b,d)
        print(maps)
        time.sleep(0.1)
        cnt += 1
    else:
        print("open")
        print("abd", a,b,d)
        cnt = 0
        a, b = mt[0], mt[1]
        maps[a][b] = -1
        result += 1

print(result+1)