# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Tree:
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.right=right
        self.left=left


root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left=Tree(15)
root.right.right=Tree(7)

def max_depth(root):
    if not root:
        return 0
    
    left=max_depth(root.left)
    right=max_depth(root.right)

    return 1+max(left,right)

x=max_depth(root)

print(x)
    