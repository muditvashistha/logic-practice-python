from collections import deque
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




def dfs(node):     #basically pre order, root,left,right
    if not node:
        return
    print(node)
    dfs(node.left)
    dfs(node.right)

def post_order(node): #left right root
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

def in_order(node): #Left → Root → Right
    in_order(node.left)
    print(node)
    in_order(node.right)






def iterative_preorder(node):
    stk=[node]
    while stk:
        node=stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left:stk.append(node.left)


def bfs(node):
    if not node:
        return
    q=deque()
    q.append(node)
    while q:
        node=q.popleft()
        print(node)
        if node.left : q.append(node.left)
        if node.right : q.append(node.right)





def search(node,target):
    if not node:
        return False
    
    if node.val==target:
        return True

    return search(node.left,target) or search(node.right, target)



def faster_search(node , target):
    if not node:
        return False
    
    if target < node.val:
        return faster_search(node.left , target)
    
    
    else: return faster_search(node.right , target)   



# def check_equal(node1 , node2):
#     if not node1:
#         return
#     if not node2:
#         return
#     tree1=[]
#     tree2=[]
#     q1=deque()
#     q1.append(node1)

#     q2=deque()
#     q2.append(node2)
#     while q1:
#         node1=q1.popleft()
#         tree1.append(node1.val)
#         if node1.left : q1.append(node1.left)
#         if node1.right : q1.append(node1.right)
    
#     while q2:
#         node2=q2.popleft()
#         tree2.append(node2.val)
#         if node2.left : q2.append(node2.left)
#         if node2.right : q2.append(node2.right)
#     for i in tree1:
#         print(i)
    
#     print("\n")

#     for i in tree2:
#         print(i)

#     res=tree1==tree2
#     print(res)
    
# check_equal(A,A1)


    
    



    


    

