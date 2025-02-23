import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  
    g_cost = {start: 0}
    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]  

        for neighbor, cost in graph[current]:
            tentative_g_cost = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    return None  

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 2)],
    'C': [('F', 5), ('G', 2)],
    'D': [],
    'E': [('H', 1)],
    'F': [],
    'G': [('H', 3)],
    'H': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4, 'D': 6, 'E': 2, 'F': 5, 'G': 3, 'H': 0
}

start_node = 'A'
goal_node = 'H'

path = a_star(graph, start_node, goal_node, heuristic)

if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")
