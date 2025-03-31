class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)
    
def display(head):
        curr=head
        elements=[]
        while curr:
            elements.append(str(curr.val))
            curr=curr.next
        print(' -> '.join(elements))

def insert_at_end(head, val):
    new_node = SinglyNode(val)
    if head is None:  # If list is empty, new node becomes the head
        return new_node
    curr = head
    while curr.next:  # Traverse to the last node
        curr = curr.next
    curr.next = new_node  # Append the new node at the end
    return head

# Taking user input
head = None
n = int(input("Enter the number of elements: "))
for _ in range(n):
    value = input("Enter value: ")
    head = insert_at_end(head, value)

display(head)
#finding the length of the linked list

curr=head
count=0
while curr:
     count+=1
     curr=curr.next

print(f'The length of the linked list is {count}')
rotations=2

effective_rotations=rotations % count

for i in range(effective_rotations):
     curr=head
     prev=None

     while curr.next is not None:
          prev=curr
          curr=curr.next
     curr.next=head
     prev.next=None
     head=curr
print("After Rotation")
display(head)

print(count)
print(2%5)



