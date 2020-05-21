'''Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]:
                    matrix[i][j] = 1+min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    print(matrix)
        return sum([sum(row) for row in matrix])
        