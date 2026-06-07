g = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':[], 'F':[]}

visited = set()

def dfs(node):
    visited.add(node)
    for i in g[node]:
        if i not in visited:
            dfs(i)

dfs('A')
print("DFS traversal:", visited)