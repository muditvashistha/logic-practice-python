import os 
import math
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

#creating the list and storing the elements in it
# ar=[]
# x=int(input("Enter the nunber of elements in the list: "))
# for j in range(0,x):
#     content=int(input("Enter the elements :"))
#     print("\t")
#     ar.append(content)



#storing the length of the list in order for us to traverse
# lambai=len(ar)

# def aVeryBigSum(ar):
#     count=0
#     for i in range(lambai):
#         count=count+ar[i]
#     print(count)
   
# aVeryBigSum(ar)

    


y="1000000001 1000000002 1000000003 1000000004 1000000005 100000000000001"
main_list=[]
ele=y.split()

for i in range(len(ele)):
    current_number=int(ele[i])
    main_list.append(current_number)

def bigsum(ar):
    count=0
    for j in range(len(ar)):
        count=count+ar[j]
    print(count)

bigsum(main_list)
