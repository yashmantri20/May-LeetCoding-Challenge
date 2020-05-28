'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0]*(num+1)
        dp[1] = 1
        for i in range(2 , num + 1):
            if i & 1 == 0:
                dp[i] = dp[i // 2] 
            else:
                dp[i] = dp[i // 2]  + 1
        return dp