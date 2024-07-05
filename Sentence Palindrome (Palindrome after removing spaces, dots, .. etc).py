# Write a program to check if a sentence is a palindrome or not. You can ignore white spaces and other characters to consider sentences as a palindrome.

# Input : str = "Too hot to hoot."
# Output : Sentence is palindrome.

# Input : str = "Abc def ghi jklm."
# Output : Sentence is not palindrome.
str="Too hot to hoot."
x=str.lower()
t=x.replace(" ","")
p=t.replace(".","")


if p==p[::-1]:
    print("Sentence is a Palindrome")
else:
    print("Sentence is not a palindrome")