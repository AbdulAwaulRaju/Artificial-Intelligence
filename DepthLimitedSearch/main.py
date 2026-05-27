# Depth Limited Search (DLS)

Depth Limited Search is a variation of Depth First Search where the search is restricted to a predefined depth limit.

## Idea
- Uses stack (DFS approach)
- Expands nodes only within a given depth limit
- Stops if goal is found or depth limit is reached

## Algorithm Steps
1. Start from the initial node
2. Explore neighbors using stack
3. Track current depth of each node
4. Do not expand nodes beyond depth limit
5. Stop when goal is found or search ends

## Time Complexity
O(b^l)

## Space Complexity
O(b × l)

Where:
- b = branching factor
- l = depth limit
