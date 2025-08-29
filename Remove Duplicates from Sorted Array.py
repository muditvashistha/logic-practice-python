# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


x=[1,1,2]
j=1

if len(x)==0 or len(x)==1: #edge case
    print("The array is empty or has just one element")
for i in range(1,len(x)): #starting from second index in order to compare with the first element
    if x[i]!=x[i-1]:
        x[j]=x[i]
        j=j+1 #counting each time j gets changed for finding a non repeating value
print(j)
print(x[:j])



