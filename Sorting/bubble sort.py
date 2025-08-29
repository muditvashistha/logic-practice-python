x=[39, 12, 18, 85, 72, 10, 2, 18]

for n in range(len(x)-1,0,-1):
    for i in range(n):
        if x[i] > x[i+1]:
            x[i] , x[i+1] = x[i+1] , x[i]

print(x)