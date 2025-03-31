# You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.

# The ith day is a good day to rob the bank if:

# There are at least time days before and after the ith day,
# The number of guards at the bank for the time days before i are non-increasing, and
# The number of guards at the bank for the time days after i are non-decreasing.

# Example 1:

# Input: security = [5,3,3,3,5,6,2], time = 2
# Output: [2,3]
# Explanation:
# On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
# On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
# No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
# Example 2:

# Input: security = [1,1,1,1,1], time = 0
# Output: [0,1,2,3,4]
# Explanation:
# Since time equals 0, every day is a good day to rob the bank, so return every day.

# for i in range(time,len(x)-time):
#     print(x[i])
#     for j in range(i,time)

# for i in range(4,time-1,-1):
#     print(i)

# for j in range(i-1,time-3,-1):
#         print(x[j],"\n")


# x=[5,3,3,3,5,6,2]
# time=2
# prev_days=[]
# post_days=[]
# access 'time' number of days before ith day
# for p in range(time,len(x)-time):
#     curr=p
#     for g in range(time,0,-1):
#         prev_days.append(x[curr-1])
#         curr=curr-1 
# print(prev_days)


# access 'time' number of days after ith day
# for j in range(time,len(x)-time):
#     curr=j
#     for g in range(time,0,-1):
#         post_days.append(x[curr+1])
#         curr=curr+1
    
# print(post_days)


x = [5,3,3,3,5,6,2]
# x=[1,2,3,4,5,6]
time = 2
days_check=0
if time==0:
    print("All the days are good days to rob the bank")
for p in range(time, len(x)-time):
    curr=p
    if x[curr-1] <= x[curr-time] and x[curr+1]<=x[curr+time]:
        days_check+=1
        print(f"day {p} is a good day to rob the bank")

if days_check == 0:
    print("No good days have been found to rob the bank!")    

