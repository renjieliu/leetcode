class Solution:
    def findKthPositive(self, arr: 'List[int]', k: int) -> int:
        arrLast = arr[-1]
        for i in range(1, arrLast+1): #complete the array
            if arr:
                if i!= arr[0]:
                    k-=1
                    if k == 0:
                        return i
                else:
                    arr.pop(0)
            else:
                break

        return arrLast+k

