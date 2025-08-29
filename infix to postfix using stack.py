expression="(A+B)*C"

output=""

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

stack=[]

for char in expression:

    if char.isalnum():
        output=output+char
    
    elif char=='(':
        stack.append(char)
    
    elif char==')':
        while stack and stack[-1]!='(':
            output=output+stack.pop()
        
        if stack and stack[-1]=='(':
            stack.pop()
    elif char in precedence:
        while stack and stack[-1]!="(" and stack[-1] in precedence and precedence[stack[-1]] < precedence[char]:
            output=output+stack.pop()
        stack.append(char)
    
while stack:
    output=output+stack.pop()


print(output)

