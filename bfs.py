
from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()


graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['G'], 'F': [], 'G': []}
bfs(graph, 'A')
