"""
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
"""

from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        friends = dict()
        for i in range(n):
            friends[i] = {i}
        # friends = {0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}, 5: {5}}

        for t, p, q in logs:
            s = friends[p].union(friends[q])
            # s = {0, 1}

            for i in s:
                friends[i] = s
                # friends[0] = {0, 1}
                # friends[1] = {0, 1}
            if n == len(s):
                return t
        return -1


# Test cases
print(Solution().earliestAcq(logs=[[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n=4))  # 3
print(Solution().earliestAcq(logs=[[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5], [20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n=6))  # 20190301
print(Solution().earliestAcq(logs=[[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], n=4))  # 2
print(Solution().earliestAcq(logs=[[6,1,5],[7,4,2],[2,1,0],[3,1,2],[4,5,3],[11,5,4],[9,1,3],[0,2,0],[1,4,3]], n=6))  # 6
