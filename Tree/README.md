# LeetCode 1028 - Recover a Tree From Preorder Traversal

## Problem Description

You are given a string `traversal` representing the preorder traversal of a binary tree where:
- Each node's value is a non-negative integer
- The depth of each node is represented by dashes (`-`) before the node's value
- The depth of the root node is 0 (no dashes)
- The depth of each child is 1 more than its parent

The goal is to recover the binary tree from this representation and return its root.

## Approach

The solution uses a level-based approach to reconstruct the tree:

1. Parse the first number from the traversal string to create the root node
2. Maintain a dictionary of nodes at each level
3. Iterate through the traversal string:
   - Count consecutive dashes to determine the current depth
   - Parse the node value that follows the dashes
   - Find the parent node (which is at depth-1)
   - Add the new node as the left child if left is empty, otherwise as the right child
   - Store the node in the appropriate level of the dictionary

This approach effectively rebuilds the tree by keeping track of potential parent nodes at each level and connecting new nodes to the correct parents based on the depth information.

## Complexity Analysis

- Time Complexity: O(n), where n is the length of the traversal string
  - We parse the string character by character once
  - Each node is processed in constant time
  
- Space Complexity: O(h), where h is the height of the tree
  - The dictionary stores at most one node per level at any time
  - In the worst case, this is proportional to the height of the tree

## Example

For the input string "1-2--3---4-5--6---7":
- Root node (level 0): 1
- Level 1: 2, 5
- Level 2: 3, 6
- Level 3: 4, 7

The solution builds the tree:
```
    1
   / \
  2   5
 /   /
3   6
/   /
4   7
```

## Note

The TreeNode class definition used in this solution provides the basic structure for a binary tree node with value, left child, and right child properties.