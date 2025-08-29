# nput : n = 5 and array[] = {1, 2, 3, 4 ,3}
# Output: 3
# Explanation: The number 3 appears more than once in the array.


x=[1, 6, 5, 2, 3, 3, 2]

element_frequency={}

def find_duplicate(x):

    for i in x:
        if i in element_frequency:
            element_frequency[i]+=1
        else:
            element_frequency[i]=1
    for key,value in element_frequency.items():
        if value>1:
            print(key)

find_duplicate(x)
