from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i >= m:
                return n - j  # insert the rest of word2[j:]
            elif j >= n:
                return m - i  # delete the rest of word1[i:]
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
		    # replace, insert, delete, respectively
            return 1 + min(dp(i + 1, j + 1), dp(i, j + 1), dp(i + 1, j))
        
        m, n = map(len, (word1, word2))
        word1, word2 = map(list, (word1, word2))
        return dp(0, 0)