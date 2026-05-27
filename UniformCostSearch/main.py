import heapq

# Graph with cost (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

start = 'A'
goal = 'G'

def ucs(graph, start, goal):

    # Priority queue stores (cost, node, path)
    pq = []
    heapq.heappush(pq, (0, start, [start]))

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        print(f"Visiting: {node}, Cost: {cost}")

        # Goal check
        if node == goal:
            print("\nGoal found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            # Explore neighbors
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    print("Goal not reachable")


# Run UCS
ucs(graph, start, goal)
