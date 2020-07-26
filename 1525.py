class Solution:
    def numSplits(self, s: str) -> int:
        right = {}
        for c in s:
            if c not in right:
                right[c] = 0
            right[c] +=1
        left = {}
        output = 0
        for c in s:
            if c not in left:
                left[c] = 0
            left[c] +=1
            if c in right:
                right[c]-=1
                if right[c] ==0:
                    del right[c]
            if len(left) == len(right):
                output+=1
        return output