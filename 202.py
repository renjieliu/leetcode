class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(n) :
            output = 0
            for c in str(n):
                output += int(c)**2
            return output
        seen = []
        curr = calc(n)
        if curr ==1 : return True
        while curr != 1 and curr not in seen:
            seen.append(curr)
            curr = calc(curr)
            if curr==1:
                return True
        return False