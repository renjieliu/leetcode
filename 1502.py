class Solution:
    def canMakeArithmeticProgression(self, arr: 'List[int]') -> bool:
        if len(arr) <= 2 : return True
        arr.sort()
        delta = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != delta:
                return False
        return True
