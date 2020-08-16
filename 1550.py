class Solution:
    def threeConsecutiveOdds(self, arr: 'List[int]') -> bool:
        odd = 0
        for a in arr:
            if a % 2 == 0:
                odd = 0
            else:
                odd += 1
                if odd == 3:
                    return True
        return False
