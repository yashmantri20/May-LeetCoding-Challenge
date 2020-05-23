class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j,ans = 0,0,[]
        while i < len(A) and j < len(B):
            al,ar = A[i]
            bl,br = B[j]
            if bl <= al <= br or al<=bl<=ar:
                ans.append([max(al,bl),min(ar,br)])
            if ar > br:
                j+=1
            elif ar  == br:
                i+=1
                j+=1
            else:
                i+=1
        return ans
        