# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)
    
def is_same(a,b):

    if not a and not b:
        return True
    
    if not a or not b:
        return False
    

    return (a.val==b.val and is_same(a.left,b.left) and is_same(a.right,b.right))


def isSubtree(root,Subtree):
    if not Subtree:
        return True
    
    if not root:
        return False
    
    if is_same(root,Subtree):
        return True
    
    return(isSubtree(root.left,Subtree) or (root.right, Subtree))   
    

    


