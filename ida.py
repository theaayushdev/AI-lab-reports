def ida_star(graph, start, goal, heuristic):
    def dfs(graph, current, goal, threshold, g_cost, heuristic, path):
        f_cost = g_cost[current] + heuristic[current]
        if f_cost > threshold:
            return float('inf')
        path.append(current)
        if current == goal:
            return path
        min_threshold = float('inf')
        for neighbor, cost in graph[current]:
            if neighbor not in path:
                g_cost[neighbor] = g_cost[current] + cost
                result = dfs(graph, neighbor, goal, threshold, g_cost, heuristic, path)
                if isinstance(result, list):
                    return result
                min_threshold = min(min_threshold, result)
        path.pop()
        return min_threshold

    threshold = heuristic[start]
    while True:
        path = []
        g_cost = {start: 0}
        result = dfs(graph, start, goal, threshold, g_cost, heuristic, path)
        if isinstance(result, list):
            return result
        if result == float('inf'):
            return None
        threshold = result

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('H', 1)],
    'F': [],
    'G': [],
    'H': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0,
    'H': 0
}

start_node = 'A'
goal_node = 'H'

path = ida_star(graph, start_node, goal_node, heuristic)
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")
