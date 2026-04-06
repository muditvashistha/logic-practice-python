from collections import defaultdict,deque
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

#creating adjacency list
M = []
for i in range(n):
    M.append([0]*n)

for v,u in A:
    M[v][u] = 1

#if undirected graph hota toh M[u][v] = 1 bhi karna padta

#creating the adjacancy list
D = defaultdict(list)
for v,u in A:
    D[v].append(u)

#dfs with recursion
def dfs_recursive(node):
    print(node)
    for x in D[node]:
        if x not in seen:
            seen.add(x)
            dfs_recursive(x)

source = 0
seen = set()
seen.add(source)

#dfs_recursive(source)  karke run karlo mast 


#dfs with stack
stk = [source]
while stk:
    node  = stk.pop()
    print(node)
    for i in D[node]:
        if i not in seen:
            seen.add(i)
            stk.append(i)


#bfs
q = deque()
q.append(source)
while q:
    node = q.popleft()
    print(node)
    for i in D[node]:
        if i not in seen:
            seen.add(i)
            q.append(i)
    