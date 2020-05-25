'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                EA = A[i-1]
                EB = B[j-1]

                dp[i][j] = dp[i-1][j-1] + 1 if EA == EB else max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
        