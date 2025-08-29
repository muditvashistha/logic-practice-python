x=[12, 11, 13, 5, 6]

for i in range(1,len(x)):
    j=i
    while j > 0 and x[j-1] > x[j]:
        x[j] , x[j-1] = x[j-1] , x[j]
        j=j-1

print(x)