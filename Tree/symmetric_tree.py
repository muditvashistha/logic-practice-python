# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



class treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)
    
A=treenode(1)
B=treenode(2)
C=treenode(2)
D=treenode(3)
E=treenode(4)
F=treenode(4)
G=treenode(3)

A.left==B
A.right=C

B.left=D
B.right=E

C.left=F
C.right=G


def symm(node1, node2):
    if not node1 and not node2:
        return True
    
    if not node1 or not node2:
        return False
    
    if node1.val != node2.val:
        return False
    
    return (symm(node1.left,node2.right) and symm(node1.right,node2.left))

