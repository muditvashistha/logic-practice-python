#to find the sums of the diagonal elements(both the diagonals) in a square matrix and then find the difference between the sums
mat=[[1,2,3],[4,5,6],[7,8,9]]
count=len(mat)
diag1=[]
diag2=[]
# traversing and storing the forward diagonals in another list
for i in range(count):
    for j in range(count):
        if(i==j):
            
            diag1.append(mat[i][j])

# traversing and stroing the backward diagonals in another list
for i in range(count):
    diag2.append(mat[i][-i-1])


print("The sum of the first set of diagonal elements in the given matrix is",sum(diag1),"and the sum of the second set of the diagonals is",sum(diag2),"and the difference between them is",abs(sum(diag1)-sum(diag2)))