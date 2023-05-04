#Leetcode 118. Pascal's Triangle
from collections import deque
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = deque()           # deque is faster than list
        for col in range(numRows):          # Time Complexity: O(n^2), Space Complexity: O(n)
            lis = deque([1])
            ans = 1
            for i in range(1, col + 1):
                ans = ans * (col + 1 - i) / i
                lis.append(ans)
            pascal_triangle.append(lis)
            
        return pascal_triangle
# Avg. Time Complexity:  O(n^2), Space Complexity: O(n^2)
# Runtime: 16 ms, Memory: 13.4 MB
