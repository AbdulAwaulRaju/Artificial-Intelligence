# Iterative Deepening Search (IDS)

def dls(graph, node, goal, depth):

    # Goal check
    if node == goal:
        return True

    # Stop if depth becomes zero
    if depth <= 0:
        return False

    # Explore neighbors
    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth - 1):
            return True

    return False


def ids(graph, start, goal, max_depth):

    # Increase depth level one by one
    for depth in range(max_depth + 1):

        print(f"Searching at depth level: {depth}")

        if dls(graph, start, goal, depth):
            print(f"\nGoal '{goal}' found at depth {depth}")
            return True

    print(f"\nGoal '{goal}' not found")
    return False


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Run IDS
ids(graph, start='A', goal='G', max_depth=5)
