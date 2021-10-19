class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == "X": #only convert when meet an X
                cnt += 1
                i+=3
            else:
                i+=1
        return cnt


