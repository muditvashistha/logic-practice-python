# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.



container=[0,1,2,2,3,0,4,2]
x=len(container)



#sorting the resultant list
def sort(container):
    for i in range(0,len(container)):
        for j in range(i+1,len(container)):
            if container[i]>=container[j]:
                container[i],container[j]=container[j],container[i]
    

#function for removing and printing elements 
def remove(container,val):

    k=0
    while 2 in container:
        container.remove(2)
        k=k+1
    sort(container)
    print(x-k,container)
    

remove(container,2)


    




                  
