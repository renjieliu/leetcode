class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K or K > 26: return 0
        i = 0
        cnt = 0
        while i < len(S)+1-K:
            t = S[i:i+K]
            if len(t) == len(set(list(t))):
                cnt +=1
            i+=1
        return cnt