import heapq

def ao_star(graph, start, goal_nodes, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))  

    cost = {start: 0}
    came_from = {}

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current in goal_nodes:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]  

        for neighbor, child_cost in graph.get(current, []):
            tentative_cost = cost[current] + child_cost

            if neighbor not in cost or tentative_cost < cost[neighbor]:
                cost[neighbor] = tentative_cost
                heapq.heappush(open_list, (tentative_cost + heuristic.get(neighbor, 0), neighbor))
                came_from[neighbor] = current

    return None  

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5), ('G', 2)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 5,
    'G': 3,
}

start_node = 'A'
goal_nodes = {'D', 'E'}

solution = ao_star(graph, start_node, goal_nodes, heuristic)
if solution:
    print(f"Solution path: {' -> '.join(solution)}")
else:
    print("No solution found.")
