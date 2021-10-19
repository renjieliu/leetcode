class Solution:
    def getLastMoment(self, n: int, left: 'List[int]', right: 'List[int]') -> int:
        A = max(left or [0]) # the last from left to finish
        B = n - min(right or [n]) #the last from right to finish
        return max(A, B)