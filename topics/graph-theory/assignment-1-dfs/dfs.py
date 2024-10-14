"""
Solution for problem 1
Try to:
    - Implement the DFS function.
    - Test it with the provided example.
"""
def dfs(graph: dict, start: str) -> list:
    visited = set()  # Set to track visited nodes
    result = []      # List to store DFS traversal order

    def dfs_helper(node):
        # Mark the current node as visited and add it to the result
        visited.add(node)
        result.append(node)
        
        # Recursively visit each neighbor of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    # Start DFS from the start node
    dfs_helper(start)

    # Return the list of visited nodes in DFS order
    return result


## Test it
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(dfs(graph, 'A'))