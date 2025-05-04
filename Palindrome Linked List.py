class SinglyNode():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)
    

    
Head=SinglyNode(1)
A=SinglyNode(2)
B=SinglyNode(2)
C=SinglyNode(2)
D=SinglyNode(1)

Head.next=A
A.next=B
B.next=C
C.next=D

def Check_palindrome(Head):
    curr=Head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    if elements==elements[::-1]:
        print(True)
    else:
        print(False)

Check_palindrome(Head)