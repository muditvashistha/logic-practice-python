# Invert Binary Tree

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Input: root = [2,1,3]
# Output: [2,3,1]


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

#defining a binary tree
class Tree:
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.right=right
        self.left=left


root = Tree(4)
root.left = Tree(2)
root.right = Tree(7)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right.left = Tree(6)
root.right.right = Tree(9)



    

def invert_tree(root):
        if not root:
            return None
        
        root.left , root.right = root.right , root.left

        invert_tree(root.left)
        invert_tree(root.right)

        return root


def print_tree(root):
    if not root:
        print("[]")
        return
    
    queue = [root]
    result = []
    
    while queue:                                                                                                
        node = queue.pop(0)                                                                                     
        if node:                                                                                                
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    
    while result and result[-1] is None:
        result.pop()
    
    print(result)

res=invert_tree(root)

print_tree(root)

print_tree(res)

