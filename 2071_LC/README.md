# LeetCode 2071 - Maximum Number of Tasks You Can Assign

## Problem Description

You are given four parameters:
- `tasks`: A list representing difficulty of each task
- `workers`: A list representing strength of each worker
- `pills`: Number of magical pills available
- `strength`: The boost of strength given by each pill

A worker can complete a task only if their strength is greater than or equal to the task's difficulty. Each worker can only be assigned to one task, and each task can only be assigned to one worker.

A worker can consume at most one magical pill that will increase their strength by `strength` units.

The goal is to find the maximum number of tasks that can be completed.

## Approach

The solution uses binary search to find the maximum number of tasks that can be completed:

1. Sort both tasks and workers arrays.
2. Define a function `check(mid)` that determines if it's possible to complete exactly `mid` tasks.
3. Inside the `check` function:
   - Create a sorted list of the strongest `mid` workers.
   - For each task (from hardest to easiest):
     - Try to assign the strongest worker without a pill.
     - If that's not possible, use a pill on the weakest capable worker.
   - Return true if all `mid` tasks can be completed.
4. Binary search to find the maximum value of `mid` where `check(mid)` is true.

## Complexity Analysis

- Time Complexity: O((m+n) log(m+n)), where n is the number of tasks and m is the number of workers
  - Sorting takes O(n log n) and O(m log m).
  - Binary search has at most O(log(min(n, m))) iterations.
  - Each check takes O(mid log mid) which is bounded by O(n log n).
  
- Space Complexity: O(min(n, m)) for the sorted list used in the check function.

## Note

This solution uses a `SortedList` data structure which is available in the `sortedcontainers` package in Python. You may need to install it using:
```
pip install sortedcontainers
```

And import it in your solution:
```python
from sortedcontainers import SortedList
```