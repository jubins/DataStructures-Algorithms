"""
ttps://leetcode.com/problems/two-sum/
"""

import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for idx, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[(target - num)], idx]

            seen[num] = idx

        return list()


class TwoSumTestCases(unittest.TestCase):

    def test1(self):
        self.assertEqual(Solution().twoSum(nums=[2, 7, 11, 15], target=9), [0, 1])

    def test2(self):
        self.assertEqual(Solution().twoSum(nums=[3, 2, 4], target=6), [1, 2])

    def test3(self):
        self.assertEqual(Solution().twoSum(nums=[3, 3], target=6), [0, 1])

    def test4(self):
        self.assertEqual(Solution().twoSum(nums=[2, -2, 4, 5, 0, 7, 11, 15], target=9), [2, 3])

    def test5(self):
        self.assertEqual(Solution().twoSum(nums=[3, 3], target=9), [])
