# Definition for a binary tree node.
# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
            self._val = val
            self._left = left
            self._right = right

            @property
            def val(self):
            return self._val

            @property
            def left(self):
            if self._val == 4:
                return None
            return self._left

            @left.setter
            def left(self, node):
            if self._val == 4:
                self._right = node
            else:
                self._left = node

            @property
            def right(self):
            return self._right

            @right.setter
            def right(self, node):
            if self._val == 4:
                pass
            else:
                self._right = node
class Solution:
    def recoverFromPreorder(self, traversal: str):
        
        head = TreeNode(int(traversal[0]))
        temp = head

        n = len(traversal)
        levels= defaultdict(list)
        dash = 1
        prev = 0
        levels[1].append(head)
        i =1
        while i < n:
            if traversal[i]=='-':
                dash +=1
                i +=1
                continue
            else:
                num = ''
                while i <n and traversal[i] != '-':
                    num += traversal[i]
                    i+=1
                
                if prev > dash:
                    x = prev-dash
                    while x-1:
                        levels[x] = []
                        x -=1
                prev = dash
                node = TreeNode(int(num))
                
                if levels[dash-1]:
                    parent = levels[dash-1][0]
                    if parent.left is None:
                        parent.left = node
                    else:
                        parent.right = node
                        levels[dash-1].pop(0)
                    levels[dash].append(node)
                dash = 1

        return temp
        
        
traversal = "1-2--3---4-5--6---7"
obj = Solution()
root = obj.recoverFromPreorder(traversal)
def leveltraverse_with_nulls(root):
    if not root:
        return
    q = [root]
    while q:
        temp = q.pop(0)
        if temp:
            print(temp.val, ' ', end='')
            q.append(temp.left)
            q.append(temp.right)
        else:
            print("null ", end='')

leveltraverse_with_nulls(root)
