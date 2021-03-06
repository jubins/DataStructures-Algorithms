"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        q = deque()
        q.append((root, 0))

        while q:
            node, val = q.popleft()
            if q and val == q[0][1]:
                node.next = q[0][0]
            else:
                node.next = None

            if node.left:
                q.append((node.left, val + 1))
            if node.right:
                q.append((node.right, val + 1))
        return root

