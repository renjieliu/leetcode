class Solution:
    def missingNumber(self, arr: 'List[int]') -> int:
        delta = ( arr[-1] - arr[0] ) // len(arr) # calcaulate delta, since the removed is not first or last item
        if delta == 0:
            return arr[0]
        else:
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != delta:
                    return arr[i-1] + delta

