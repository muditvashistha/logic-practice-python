x=[[1,2,3],[4,5,6],[7,8,9]]

for i in x:
    print(i)
        
result=[[0]*len(x) for i in range(len(x))]

for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]=x[j][i]

print("\n")

for i in result:
    print(i)