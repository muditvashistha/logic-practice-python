#  * 
#  *  * 
#  *  *  * 
#  *  *  *  * 
#  *  *  *  *  * 

for i in range(5):
    print(" * "*(i+1),sep=" ")

print("\n")



# *  *  *  *  * 
# *  *  *  * 
# *  *  * 
# *  * 
# * 

for i in range(5,0,-1):
    print(" * "*(i))

print("\n")

#      *
#     **
#    ***
#   ****
#  *****

x=5 #this value can be anything depending on the length of the pattern we want

for i in range(x):
    print(" "*(x-1-i), "*"*(i+1))


print("\n")


# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****


p1=[]

for i in range(5):
    p1.append("*"*(i+1))


p2=[]
x=5

for i in range(x):
    p2.append(" "*(x-1-i)+"*"*(i+1))

for line1, line2 in zip(p1, p2):
    print(line1.ljust(5) + "  " + line2)

print("\n")



# *********
#  *******
#   *****
#    ***
#     *

x = 5
for i in range(x):
    spaces = " " * i
    stars = "*" * (2 * (x - i) - 1)
    print(spaces + stars)

print("\n")

#     *
#    ***
#   *****
#  *******
# *********

x = 5
for i in range(x):
    spaces = " " * (x - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

print("\n")

# *********
#  *******
#   *****
#    ***
#     *
#     *
#    ***
#   *****
#  *******
# *********

x = 5
for i in range(x):
    spaces = " " * i
    stars = "*" * (2 * (x - i) - 1)
    print(spaces + stars)

x = 5
for i in range(x):
    spaces = " " * (x - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

print("\n")

#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


for i in range(x):
    spaces = " " * (x - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
for i in range(x):
    spaces = " " * i
    stars = "*" * (2 * (x - i) - 1)
    print(spaces + stars)

print("\n")

#  * 
#  *  * 
#  *  *  * 
#  *  *  *  * 
#  *  *  *  *  * 
# *  *  *  *  * 
# *  *  *  * 
# *  *  * 
# *  * 
# * 

for i in range(5):
    print(" * "*(i+1),sep=" ")
for i in range(5,0,-1):
    print(" * "*(i))

print("\n")




#   * 
#     * 
#       * 
#     * 
#   * 
#    *
#     *
#   * 
#     * 
#       * 
#   *
#     *
#       *
#     *
#   *
#    *
#     *
#   *
#     *
#       *
#   *
#     *
#       *
#     *
#   *
#    *
#     *
#   *
#     *
#       *

n=3

for x in range(n):
    for i in range(3):
        print("  "*i," * ")

    for i in range(1,-1,-1):
        print("  "*i," * ")
    
    for i in range(2):
        print(" "," "*(i),"*")

    for i in range(3):
        print("  "*i," * ")


