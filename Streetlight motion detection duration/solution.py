A=[1, 3, 5]
B= 2
duration_list=[]

for i in A:
    temp=i
    for j in range(B):
        duration_list.append(temp)
        temp = temp + 1

print(len(set(duration_list)))

# class Solution:
#     # @param A : list of integers (motion detection times)
#     # @param B : integer (duration in seconds)
#     # @return an integer (total time light remains on)
#     def totalTime(self, A, B):
#         duration_list=[]
#         for i in A:
#             temp=i
#             for j in range(B):
#                 duration_list.append(temp)
#                 temp=temp+1
#         return len(set(duration_list))
    





