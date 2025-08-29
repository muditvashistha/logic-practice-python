x=[-2, 45, 0, 11, -9,88,-97,-202,747]

for i in range(len(x)):
    curr_min=i
    for p in range(i+1,len(x)):
        if x[p] < x[curr_min]:
            curr_min=p
    x[i] , x[curr_min] = x[curr_min] , x[i]

            

print(x) 