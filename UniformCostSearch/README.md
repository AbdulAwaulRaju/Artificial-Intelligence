# Uniform Cost Search (UCS)

Uniform Cost Search is an uninformed search algorithm that finds the least cost path from the start node to the goal node.

## Idea
- Always expands the node with the lowest path cost
- Uses a priority queue (min heap)
- Guarantees optimal solution

## Algorithm Steps
1. Start from initial node with cost 0
2. Insert into priority queue
3. Always pick lowest cost node
4. Expand neighbors and update cost
5. Stop when goal is reached

## Time Complexity
O(E log V)

## Space Complexity
O(V)

## 특징
- Optimal solution guaranteed
- Similar to Dijkstra’s algorithm
