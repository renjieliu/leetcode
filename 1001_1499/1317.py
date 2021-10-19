class Solution:
    def getNoZeroIntegers(self, n: int) -> 'List[int]':
        for i in range(n):
            for j in range(n):
                if i+j == n and str(i).count('0') == str(j).count('0') ==0:
                    return [i,j]