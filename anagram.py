#Given two strings. The task is to check whether the given strings are anagrams of each other or not. 
# An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

# Input: str1 = “listen”  str2 = “silent”
# Output: “Anagram”
# Explanation: All characters of “listen” and “silent” are the same.

# Input: str1 = “gram”  str2 = “arm”
# Output: “Not Anagram”

x="listen"
y="silent"



#by using the sorted function
def check_anagram(str1,str2):
    if len(str1)==len(str2):
        if sorted(x)==sorted(y):
            print("Anagram")
        else:
            print("Not Anagram")
    else:
        print("Not Anagram")

check_anagram(x,y)

#without using sorted function
dict_x={}
dict_y={}

for i in x:
    if i in dict_x:
        dict_x[i]+=1
    else:
        dict_x[i]=1

for i in y:
    if i in dict_y:
        dict_y[i]+=1
    else:
        dict_y[i]=1

if dict_x==dict_y:
    print("Anagram")
else:
    print("Not Anagram")





