def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)


graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['G'], 'F': [], 'G': []}
visited = set()
print("DFS Traversal:", end=" ")
dfs_recursive(graph, 'A', visited)
print()
