# Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
# Output: 10
# Explanation: The expected rainwater to be trapped is shown in the above image.

# Input: arr[]   = {3, 0, 2, 0, 4}
# Output: 7
# Explanation: Structure is like below.
# We can trap “3 units” of water between 3 and 2,
# “1 unit” on top of bar 2 and “3 units” between 2 and 4.


arr=[3, 0, 2, 0, 4]
n=len(arr)
answer=0
if n<1:
    print("Cannot store any water!")

left_max=[0]*n
right_max=[0]*n

left_max[0]=arr[0]

for i in range(1,n):
    left_max[i]=max(left_max[i-1],arr[i])

right_max[-1]=arr[-1]

for i in range(n-2,-1,-1):
    right_max[i]=max(right_max[i+1],arr[i])

for i in range(n):
    answer+=min(left_max[i],right_max[i])-arr[i]

print(answer)