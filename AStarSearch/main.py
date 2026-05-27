import heapq

# Graph: (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

# Heuristic values (estimated cost to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'


def a_star(graph, start, goal):

    # Priority queue: (f = g + h, g, node, path)
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))

    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        print(f"Visiting: {node}, g={g}, f={f}")

        # Goal check
        if node == goal:
            print("\nGoal found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    print("Goal not reachable")


# Run A* Search
a_star(graph, start, goal)
