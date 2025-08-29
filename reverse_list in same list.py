l=[1,2,3,4,5,6,7]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])


# temp=0
# for i in range(len(l)):
#     for j in range(len(l)-1,-1,-1):
        
#         temp=l[i]
#         l[i]=l[j]
#         l[j]=temp
        
# print(l)


# temp=0
# temp=l[0]
# l[0]=l[6]
# l[6]=temp
# print(l)
     

for i in range(len(l)//2):
    
        
    l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]

print(l)