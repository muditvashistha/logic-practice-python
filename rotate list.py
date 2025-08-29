# Given a singly linked list and an integer k, the task is to rotate the linked list to the left by k places.

# Input: linked list = 10 -> 20 -> 30 -> 40 -> 50, k = 4
# Output: 50 -> 10 -> 20 -> 30 -> 40


class LinkedList:
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



linked_lists_items=[10,20,30,40,50]


head=None
tail=None
for i in linked_lists_items:
    new_node=LinkedList(i)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node
print("Original Linked List")
display(head)

k=2
effective_rotations=k % len(linked_lists_items)

for i in range(effective_rotations):
     curr=head
     prev=None

     while curr.next is not None:
          prev=curr
          curr=curr.next
     curr.next=head
     prev.next=None
     head=curr
print("After rotation")
display(head)
