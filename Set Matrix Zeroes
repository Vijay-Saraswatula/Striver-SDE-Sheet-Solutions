# 73. Set Matrix Zeroes
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])

        row_index = [True for i in range(no_of_rows)]   # Time Complexity: O(n),    Space Complexity: O(n)
        col_index = [True for j in range(no_of_cols)]   # Time Complexity: O(n),    Space Complexity: O(n)
        empty_row = [0 for k in range(no_of_cols)]      # Time Complexity: O(n),    Space Complexity: O(n)

        for row in range(no_of_rows):                   # Time Complexity: O(n^2),  Space Complexity: O(1)
            for col in range(no_of_cols):
                if matrix[row][col] == 0:
                    row_index[row] = False
                    col_index[col] = False

        for i in range(no_of_rows):                     # Time Complexity: O(n * log(n)),  Space Complexity: O(1)
            if row_index[i]:
                for j in range(no_of_cols):
                    if not col_index[j]:
                        matrix[i][j] = 0
            else:
                matrix[i] = empty_row

# Avg. Time Complexity: O(n^2) + O(n * log(n)),  Space Complexity: O(n)
# Runtime: 107 ms, Memory: 14.3 MB
