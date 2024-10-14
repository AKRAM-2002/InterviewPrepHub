# Assignment 4: Lockboxes Problem

## Problem Description
You have `n` boxes, each of which may contain some keys. A key can unlock another box, and initially, you have the key to open the first box (box 0). Write a method to determine if all the boxes can be opened.

- Each box is numbered sequentially from 0 to `n - 1`.
- Each box contains a list of keys, where each key is represented by an integer corresponding to the box it unlocks.

### Example:
```python
boxes = [[1], [2], [3], []]
# Starting with box 0, you can unlock all the boxes.
# Output: True
```
### Solution:
#### Graph Representation:
- Each box is represented as a node.
- A key acts as an edge between nodes (boxes).

#### Algorithm:
- Use a stack or queue to explore the boxes.
- Track which boxes you’ve unlocked.
- Stop when no more boxes can be unlocked.