# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1

class treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return (self.val)
    
A=treenode(1)
B=treenode(2)
C=treenode(3)
D=treenode(4)
E=treenode(5)

A.left=B
A.right=C

B.left=D
B.right=E

def diameter(node):
    largest_dia=[0]

    def find_height(node):
        if not node:
            return 0
        
        left=find_height(node.left)
        right=find_height(node.right)
        diameter=left+right

        largest_dia[0]=max(largest_dia[0] , diameter)
    
        return 1+max(left,right)
    find_height(node)
    return largest_dia[0]

print(diameter(A))