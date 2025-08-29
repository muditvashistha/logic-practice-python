# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false


class treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)
    
A=treenode(1)
B=treenode(2)
C=treenode(3)
D=treenode(5)
E=treenode(10)

A.left=B
A.right=C
C.left=D
C.right=E


A1=treenode(1)
B1=treenode(2)
C1=treenode(3)
D1=treenode(5)
E1=treenode(10)

A1.left=B1
A1.right=C1
C1.left=D1
C1.right=E1




def is_equal(node1 , node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2 or node1.val != node2.val:
        return False

    return(is_equal(node1.left,node2.left)) and is_equal(node1.right , node2.right) 
print(is_equal(A,A1))