# A* Search Algorithm

A* Search is an informed search algorithm that finds the shortest path using both actual cost and heuristic cost.

## Formula
f(n) = g(n) + h(n)

Where:
- g(n) = cost from start to current node
- h(n) = estimated cost to goal

## Idea
- Uses priority queue
- Expands node with lowest f(n)
- Combines UCS + Greedy Best First

## Advantages
- Optimal solution (if heuristic is admissible)
- Faster than UCS in many cases

## Time Complexity
O(E log V)

## Space Complexity
O(V)
