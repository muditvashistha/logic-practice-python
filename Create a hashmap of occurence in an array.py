x=[0,0,1,1,1,2,2,3,3,4]
dict={}

#created a base dictionary to store each element as a key and then update its value as the occurence increases
for i in x:
    dict[i]=0

check_list=list(dict.keys())


#checking how many times does the particular key occurs in check_list and theh incrementing its value
for j in x:
    if j in check_list:
        dict[j]=dict[j]+1


print(dict)

