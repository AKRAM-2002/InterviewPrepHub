# Assignment 2: Breadth-First Search (BFS) Implementation

## Problem:
Write a function to implement BFS traversal on an undirected graph.

### Input:
- An adjacency list representation of a graph.
- A starting node.

### Output:
- A list of nodes visited in BFS order.

### Example:
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
