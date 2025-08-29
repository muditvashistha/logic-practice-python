class treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)
    

def hasPathSum(node,target):
    def path(node,curr):
        if not node:
            return False
        curr=curr+node.val

        if not node.right and not node.left:
            return curr ==  target
        
        return path(node.left,curr) or path(node.right,curr)
    
    return path(node,0)
   
