# Iterative Deepening Search (IDS)

Iterative Deepening Search is a combination of Depth First Search (DFS) and Breadth First Search (BFS).

It repeatedly performs Depth Limited Search with increasing depth levels until the goal node is found.

## Idea
- Start searching from depth 0
- Increase depth step by step
- Perform DLS at each depth level

## Advantages
- Uses less memory than BFS
- Finds shallow goal efficiently

## Time Complexity
O(b^d)

## Space Complexity
O(b × d)

Where:
- b = branching factor
- d = depth of solution
