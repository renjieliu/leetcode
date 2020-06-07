class Solution:
    def getStrongest(self, arr: 'List[int]', k: int) -> 'List[int]':
        arr.sort(reverse = True)
        median = arr[::-1][(len(arr)-1)//2] #if len(arr)%2 != 0 else (arr[len(arr)//2-1] + arr[len(arr)//2])/2
        s = sorted(arr, key = lambda x: abs(x - median), reverse = True)
        cnt = 0
        output = []
        while cnt < k:
            output.append(s.pop(0))
            cnt += 1
        return output