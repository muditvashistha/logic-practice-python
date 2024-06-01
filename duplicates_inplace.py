x=[0,0,1,1,1,2,2,3,3,4]

def duplicate_remove(lst):
    i = 0
    while i < len(lst):
        if lst[i] in lst[:i]:
            del lst[i]
        else:
            i += 1
    return lst


duplicate_remove(x)
print(x)  

