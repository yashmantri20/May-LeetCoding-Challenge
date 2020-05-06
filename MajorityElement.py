'''Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = []
        counts = collections.Counter(nums)
        length = len(nums)
        n = length//2
        for i in counts:
            if counts[i] > n:
                i = str(i)
                s = "".join(i)
        return s