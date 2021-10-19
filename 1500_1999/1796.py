class Solution:
    def secondHighest(self, s: str) -> int:
        lkp = set()
        for c in s: #add number to the set
            if 48 <= ord(c) <= 57:
                lkp.add(c)
        if len(lkp) <= 1 :
            return -1
        return sorted(list(lkp))[-2] #find the second largest one

