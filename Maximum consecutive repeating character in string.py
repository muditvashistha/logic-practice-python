# Given a string, the task is to find the maximum consecutive repeating character in a string.
# Note: We do not need to consider the overall count, but the count of repeating that appears in one place.
# Examples: 

# Input : str = "geeekk"
# Output : e
# Input : str = "aaaabbcbbb"
# Output : a

x="geeekk"
p=len(x)
start=x[0]
count=0

for i in range(p):
    point=1
    for j in range(i+1,p):
        if(x[i]!=x[j]):
            break
        point+=1
    if point>count:
        count=point
        start=x[i]

print(start)