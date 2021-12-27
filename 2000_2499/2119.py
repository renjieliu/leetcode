class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 != 0 or num == 0 #num == 0 or num does not end with 10.

