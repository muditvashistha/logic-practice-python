
# Input: S = “504”
# Output: “5”
# Explanation: The only substring “5” is an odd number.


# Input: S = “2042”
# Output: “”
# Explanation: All the possible non-empty substrings have even values.

x="420"
for i in range(len(x),0,-1):
    if int((x[:i])) % 2 !=0:
        print(x[:i])
        break
    else:
        print("none found")
        break