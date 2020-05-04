'''Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.'''


class Solution:
    def findComplement(self, num: int) -> int:
        bin(num)
        b = ''
        a = format(num,'b')
        for i in a:
            if i == '1':
                b = b + '0'
            else:
                b = b + '1'
        return int(b,2)